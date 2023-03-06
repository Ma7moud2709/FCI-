#include<iostream>
using namespace std;
int main()
{
  int n1,n2,i,j;
  cout<<"Enter the no. of elements of the 1st array: ";
  cin>>n1;

  /* declaring arr1 of size n1 */
  int arr1[n1];
  /* Enter distinct elements */
  cout<<"Enter the elements of the 1st array: \n";
  for(i=0;i<n1;i++)
  {
    cout<<"arr1["<<i<<"]: ";
    cin>>arr1[i];
  }

  cout<<"\nEnter the no. of elements of the 2nd array: ";
  cin>>n2;

  /* declaring arr2 of size n2 */
  int arr2[n2];
  /* Enter distinct elements */
  cout<<"Enter the elements of the 2nd array: \n";
  for(i=0;i<n2;i++)
  {
      cout<<"arr2["<<i<<"]: ";
    cin>>arr2[i];
  }


  //int k = 0;
  //int intersection[k];
  /* printing elements that are common in both the arrays */
  cout<<"\nThe intersection of the two arrays: ";
  for(i=0;i<n1;i++)
  {
    for(j=0;j<n2;j++)
    {
      if(arr1[i]==arr2[j])
      {
        cout<<arr1[i]<<" ";
        //intersection[k]=arr1[i];
        //k++;
      }
    }
  }
  //for(int p=0;p<k;p++){cout<<intersection[p]<<" ";}

  return 0;
}
