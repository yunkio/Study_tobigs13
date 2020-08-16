{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function 모음"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def vector_add(v, w):\n",
    "    \"\"\"adds two vectors componentwise\"\"\"\n",
    "    return [v_i + w_i for v_i, w_i in zip(v,w)]\n",
    "\n",
    "def dot(v, w):\n",
    "    \"\"\"v_1 * w_1 + ... + v_n * w_n\"\"\"\n",
    "    return sum(v_i * w_i for v_i, w_i in zip(v, w))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PyTorch&Tensorflow",
   "language": "python",
   "name": "pytorch"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
