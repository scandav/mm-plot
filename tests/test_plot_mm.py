import unittest
import numpy as np
from mmplot.plot_mm import plot_mm
import os

class TestPlotMM(unittest.TestCase):

    def test_valid_input(self):
        mm_array = np.random.rand(3, 4, 4) * 2 - 1  # Random values between -1 and 1
        wavelengths = [450, 550, 650]
        try:
            plot_mm(mm_array, wavelengths)
        except Exception as e:
            self.fail(f"plot_mm raised an exception unexpectedly: {e}")

    def test_invalid_mm_array_shape(self):
        mm_array = np.random.rand(3, 4, 3)  # Invalid shape
        wavelengths = [450, 550, 650]
        with self.assertRaises(ValueError):
            plot_mm(mm_array, wavelengths)

    def test_mismatched_wavelengths_length(self):
        mm_array = np.random.rand(3, 4, 4)
        wavelengths = [450, 550]  # Mismatched length
        with self.assertRaises(ValueError):
            plot_mm(mm_array, wavelengths)

    def test_output_file(self):
        mm_array = np.random.rand(1, 4, 4) * 2 - 1
        wavelengths = [550]
        output_file = "test_plot.png"
        plot_mm(mm_array, wavelengths, output_file=output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == "__main__":
    unittest.main()