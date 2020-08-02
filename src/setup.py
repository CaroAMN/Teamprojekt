import setuptools


setuptools.setup(
    name="ProteomicLFQ Application", 
    version="1.0.0",
    author="Carolin Schwitalla, Hristian Gabrovski, Alexander Gebhard",
    url="https://github.com/CaroAMN/Teamprojekt/tree/Mainapp_Caro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)