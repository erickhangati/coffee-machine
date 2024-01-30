## **Coffee Machine Project**

This project implements a simple coffee machine program in Python. Users can choose from three coffee options (espresso, latte, cappuccino), view a report of remaining resources, and turn off the coffee machine. The program checks the availability of resources and the sufficiency of funds before processing each order.

## **Getting Started**

1.  Clone the repository:
    
    ```plaintext
    git clone https://github.com/your-username/your-repo.git
    ```
    
2.  Change into the project directory:
    
    ```plaintext
    cd your-repo
    ```
    
3.  Run the program:
    
    ```plaintext
    python coffee_machine.py
    ```
    

## **Usage**

1.  When prompted, enter your choice of coffee ("espresso", "latte", or "cappuccino").
2.  To view the remaining resources, type "report".
3.  To turn off the coffee machine, type "off".

## **Functionality**

*   **print\_report():** Displays the remaining resources and the amount of money in the coffee machine.
*   **check\_resources(ordered\_ingredients):** Checks if there are sufficient resources for the selected coffee option.
*   **calculate\_coins():** Prompts the user to insert coins and calculates the total amount.
*   **calculate\_change(paid, price):** Calculates the change to be returned to the user.
*   **update\_resources(ingredients):** Updates the resources and the amount of money in the coffee machine after a successful transaction.
