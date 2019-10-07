import java.util.Scanner;
public class Hacker {
 
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int arr1[]=new int[100000];
		int arr2[]=new int[100000];
		int res[]=new int[100000];
		for (int i=0;i<n;i++)
		{
			arr1[i]=sc.nextInt();
		}
		for (int j=0;j<n;j++)
		{
			arr2[j]=sc.nextInt();
		}
		for (int k=0;k<n;k++)
		{
			res[k]=arr1[k]+arr2[k];
		}
		for (int i=0;i<n;i++)
		{
			System.out.print(res[i]+" ");
		}
 
	}
 
}
