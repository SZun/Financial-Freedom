# Financial Freedom

## Description:

This product advises users on how to allocate their money (savings) by focusing on the investing and debt repayment aspects of one's finances. For investments, the calcualtor allows a user to add the balance, contribution, employer match and portfolio mix of a 401-K account. For debt, the calculator allows a user to add the debt, and the respective interest rate, for two credit cards. Additionally, the calculator also advises a user on their ideal portfolio mix based on their age. Using all these inputs, the calculator provides advice on how the capital should be allocated and how the assets should be invested (ideal portfolio mix). Furthermore, the calcualtor provides a comparison of the "with advice" and "without advice" financial outlook of an individual. The calcualtor generated the "simplified net worth" as the final output which provides a hollistic representation of the finances outlook of an individual.   

A few important details about the inner workings of the financial calculator: 

- The calcualtor uses the historical equity and fixed income markets to calculate the expected returns of various portfolio types. These expected returns are used to make the projections for the portfolio returns and balance 
- The calcualtor uses the individual salary and 2023 tax brackets to calculate the tax liability of an individual. Additionally, the calcualtor also takes into account the impact of 401 K contributions resulting in a reduction of the taxable income. This is used to calcualte the effective tax rate of an individual 
- The calcualtor uses the expcted portfolio return and cost of debt to determine how capital should be allocated. By doing so the calculator maximizes the financial health of an individual. 
- The calculator takes into account the interest cost of outstanding debt when determining how capital should be allocated.   
<hr>

## [Presentation Video (COMING SOON)](https://youtu.be/COMING_SOON)

<hr>

## The App in Use

![Financial Calculator Demo](.\assets\gifs\financial_freedom_demo_recording.gif)

## Getting Started
### Prerequisites

You must have Python 3, Anaconda, Conda and Pip installed

```
$ python3 --version
Output: Python 3.10.8
$ anaconda --version
Output: anaconda Command line client (version 1.11.0)
$ conda --verison
Output: conda 22.9.0
$ pip --verison
Ouput: pip 22.2.2 from /Users/{#Username}/opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)
```

### Cloning Repo, Installing Dependencies & Running Application
```
$ git clone git@github.com:SZun/Financial-Freedom.git
$ cd Financial-Freedom
$ sh install.sh
$ streamlit run app.py
```

## Projections

<hr>

![Simplified Net Worth Plot](.\assets\images\plots\Simplified_Net_Worth.png) | ![year End Debt Plot](.\assets\images\plots\Year-End_Debt.png)
![Investing Capital Plot](.\assets\images\plots\Investing_Capital.png) | ![Ending 401 K Balance Plot](.\assets\images\plots\Ending_401k_Balance.png)


## Built With
<hr>

- [![Python 3.7.13](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-3713/)
[![Python](https://img.shields.io/badge/Python-3.7.13-blue)](https://www.python.org/downloads/release/python-3713/) *Programming Language*
- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/) *Web app generation tool* 
- [![Conda](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/en/latest/) *Package manager*
- [![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.anaconda.com/) *Package manager*
- [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/) *Data Science Package*
- [![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/doc/) *Data Science Package*
- [Plotnine](https://plotnine.readthedocs.io/en/stable/) *Visualization Package*
- [Pillow](https://pillow.readthedocs.io/en/stable/) *Image Manipulation Package*

## Contributors
- **Sami Naeem** - [LinkedIn](https://www.linkedin.com/in/samimuhammad/) | [Github](https://github.com/sami-naeem)
- **Sam Farrell** - [Linekdin](https://www.linkedin.com/in/samuelcfarrell/) | [Github](https://github.com/SamCFarrell)
- **Sam G. Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [Github](https://github.com/SZun)
- **Max Heatter** - [LinkedIn](https://www.linkedin.com/in/maxwell-heatter-ba4b03194/) | [Github](https://github.com/MaxHeatter)