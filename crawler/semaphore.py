from threading import BoundedSemaphore

""" A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each 
release() call. 
"""
pool_sema = BoundedSemaphore()
