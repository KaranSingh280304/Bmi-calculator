{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b2465f4d",
   "metadata": {},
   "source": [
    "# BMI Calculator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1e5381d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your weight in kilograms: 93\n",
      "Enter your height in meters: 1.8\n",
      "\n",
      "Your BMI is: 28.70\n",
      "Classification: Overweight\n"
     ]
    }
   ],
   "source": [
    "#Bmi Formula\n",
    "def calculate_bmi(weight, height):\n",
    "    bmi = weight / (height ** 2)\n",
    "    return bmi\n",
    "#Classify the categories \n",
    "def classify_bmi(bmi):\n",
    "    if bmi < 18.5:\n",
    "        return \"Underweight\"\n",
    "    elif 18.5 <= bmi < 24.9:\n",
    "        return \"Normal weight\"\n",
    "    elif 25 <= bmi < 29.9:\n",
    "        return \"Overweight\"\n",
    "    else:\n",
    "        return \"Obese\"\n",
    "#Take the input form user\n",
    "def main():\n",
    "    try:\n",
    "        weight = float(input(\"Enter your weight in kilograms: \"))\n",
    "        height = float(input(\"Enter your height in meters: \"))\n",
    "    except ValueError:\n",
    "        print(\"Please enter valid numeric values for weight and height.\")\n",
    "        return\n",
    "\n",
    "    if weight <= 0 or height <= 0:\n",
    "        print(\"Weight and height must be positive values.\")\n",
    "        return\n",
    "\n",
    "    bmi = calculate_bmi(weight, height)\n",
    "    category = classify_bmi(bmi)\n",
    "\n",
    "    print(f\"\\nYour BMI is: {bmi:.2f}\")\n",
    "    print(f\"Classification: {category}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca6f1833",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
