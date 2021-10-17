import unittest
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from best_3_cntry import get_best_3_country


expect_file_path = 'expected_best_three_countries.csv'
expect_df = pd.read_csv(expect_file_path)
curr_df = pd.read_csv('best_3_countries.csv')


class TestSum(unittest.TestCase):


    def test_recovery_ratio(self):

        for i,j in zip(expect_df['Recovery_Ratio'],curr_df['Recovery_Ratio']):
            self.assertEqual(round(i,3),round(j,3),"Recovery Ratio should be {}".format(j))


    def test_death_ratio(self):

        for i,j in zip(expect_df['Death_Ratio'],curr_df['Death_Ratio']):
            self.assertEqual(round(i,3),round(j,3),"Death Ratio should be {}".format(j))
            
        
    def test_tests_ratio(self):

        for i,j in zip(expect_df['Tests_Ratio'],curr_df['Tests_Ratio']):
            self.assertEqual(round(i,3),round(j,3),"Tests Ratio should be {}".format(j))
            

if __name__ == '__main__':
    unittest.main()
