FROM python:3.11.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory inside the container
WORKDIR /Users/nyala/infiniqo/Scripts/company_stocks/stocks_web

# Copy the entire directory containing your application code to the container
COPY . .

# Install dependencies from requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Expose any necessary ports
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

