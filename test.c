/* i.e., 64KB.  The array needs to be at least twice the size of the
   8KB cache so that the array doesn't fit in memory. */
#define ARRAY_SIZE 64*1024

#define NUM_LOOPS 10000000

int main()
{
  _Alignas(64)  /* make sure that the array aligns with the cache. */
  char array[ARRAY_SIZE];
  register int outer_loop;
  register int inner_loop;
  register int solution = 0;

  for (outer_loop = 0; outer_loop < NUM_LOOPS; outer_loop++)
    {
      for (inner_loop = 0; inner_loop < ARRAY_SIZE; inner_loop++)
        {
          solution *= array[0];
          solution *= array[8224];
        }
    }
  return solution;
}
