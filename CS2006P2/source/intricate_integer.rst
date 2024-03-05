IntricateInteger
================

.. py:class:: IntricateInteger

   Initializes an intricate integer object.

   :param obj: (int) The integer value.
   :param n: (int) The modulus.
   :param alpha: (int) The multiplier.

   :raises ValueError: If modulus, multiplier, or integer are invalid.

.. py:method:: __str__()

   Returns a string representation of the intricate integer.

   :returns: (str) A string representing the intricate integer in the format "<obj mod n | alpha>".

.. py:method:: __mul__(other)

   Performs multiplication operation between two intricate integers.

   :param other: (IntricateInteger) The other intricate integer to multiply with.

   :returns: (IntricateInteger) A new intricate integer as a result of the operation.

   :raises TypeError: If the other argument is not an IntricateInteger.
   :raises ValueError: If the IntricateIntegers do not share the same modulus and alpha.

IntricateIntegers
==================

.. py:class:: IntricateIntegers

   Initializes a collection of intricate integers.

   :param n: (int) The modulus.
   :param alpha: (int) The multiplier.

.. py:method:: __str__()

   Returns a string representation of the collection of intricate integers.

   :returns: (str) A string representing the collection of intricate integers.

.. py:method:: size()

   Returns the number of intricate integers in the collection.

   :returns: (int) The number of intricate integers.

.. py:method:: __iter__()

   Initializes the iterator for the collection of intricate integers.

   :returns: (Iterator) An iterator object.

.. py:method:: __next__()

   Iterates through the collection of intricate integers.

   :returns: (IntricateInteger) The next intricate integer in the collection.

   :raises StopIteration: If there are no more elements to iterate over.
