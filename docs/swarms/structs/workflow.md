# Module/Class Name: Workflow
===========================

The `Workflow` class is a part of the `swarms` library and is used to create and execute a workflow of tasks. It provides a way to define a sequence of tasks and execute them in order, with the output of each task being used as the input for the next task.

## Overview and Introduction
-------------------------

The `Workflow` class is designed to simplify the execution of a series of tasks by providing a structured way to define and execute them. It allows for sequential execution of tasks, with the output of each task being passed as input to the next task. This makes it easy to create complex workflows and automate multi-step processes.


## Class Definition: Workflow


The `Workflow` class is a powerful tool provided by the `swarms` library that allows users to create and execute a sequence of tasks in a structured and automated manner. It simplifies the process of defining and executing complex workflows by providing a clear and intuitive interface.

## Why Use Workflows?
------------------

Workflows are essential in many domains, including data processing, automation, and task management. They enable the automation of multi-step processes, where the output of one task serves as the input for the next task. By using workflows, users can streamline their work, reduce manual effort, and ensure consistent and reliable execution of tasks.

The `Workflow` class provides a way to define and execute workflows in a flexible and efficient manner. It allows users to define the sequence of tasks, specify dependencies between tasks, and execute them in order. This makes it easier to manage complex processes and automate repetitive tasks.

## How Does it Work?
-----------------

The `Workflow` class consists of two main components: the `Task` class and the `Workflow` class itself. Let's explore each of these components in detail.

### Task Class

The `Task` class represents an individual task within a workflow. Each task is defined by a string description. It contains attributes such as `parents`, `children`, `output`, and `structure`.

The `parents` attribute is a list that stores references to the parent tasks of the current task. Similarly, the `children` attribute is a list that stores references to the child tasks of the current task. These attributes allow for the definition of task dependencies and the establishment of the workflow's structure.

The `output` attribute stores the output of the task, which is generated when the task is executed. Initially, the output is set to `None`, indicating that the task has not been executed yet.

The `structure` attribute refers to the `Workflow` object that the task belongs to. This attribute is set when the task is added to the workflow.

The `Task` class also provides methods such as `add_child` and `execute`. The `add_child` method allows users to add child tasks to the current task, thereby defining the workflow's structure. The `execute` method is responsible for executing the task by running the associated agent's `run` method with the task as input. It returns the response generated by the agent's `run` method.

### Workflow Class

The `Workflow` class is the main class that orchestrates the execution of tasks in a workflow. It takes an agent object as input, which is responsible for executing the tasks. The agent object should have a `run` method that accepts a task as input and returns a response.

The `Workflow` class provides methods such as `add`, `run`, and `context`. The `add` method allows users to add tasks to the workflow. It returns the newly created task object, which can be used to define task dependencies. The `run` method executes the workflow by running each task in order. It returns the last task in the workflow. The `context` method returns a dictionary containing the context information for a given task, including the parent output, parent task, and child task.

The `Workflow` class also has attributes such as `tasks` and `parallel`. The `tasks` attribute is a list that stores references to all the tasks in the workflow. The `parallel` attribute is a boolean flag that determines whether the tasks should be executed in parallel or sequentially.

When executing the workflow, the `run` method iterates over the tasks in the workflow and executes each task in order. If the `parallel` flag is set to `True`, the tasks are executed in parallel using a `ThreadPoolExecutor`. Otherwise, the tasks are executed sequentially.

## Benefits and Use Cases
----------------------

The `Workflow` class provides several benefits and use cases:

-   Automation: Workflows automate multi-step processes, reducing manual effort and increasing efficiency. By defining the sequence of tasks and their dependencies, users can automate repetitive tasks and ensure consistent execution.

-   Flexibility: Workflows can be easily customized and modified to suit specific needs. Users can add, remove, or rearrange tasks as required, allowing for dynamic and adaptable workflows.

-   Error Handling: Workflows provide a structured approach to error handling. If an error occurs during the execution of a task, the workflow can be designed to handle the error gracefully and continue with the remaining tasks.

-   Collaboration: Workflows facilitate collaboration by providing a shared structure for task execution. Multiple users can contribute to the workflow by adding or modifying tasks, enabling teamwork and coordination.

-   Reproducibility: Workflows ensure reproducibility by defining a clear sequence of tasks. By following the same workflow, users can achieve consistent results and easily reproduce previous analyses or processes.

Overall, the `Workflow` class is a valuable tool for managing and executing complex processes. It simplifies the creation


## Class Parameters
----------------

-   `agent` (Any): The agent object that will be used to execute the tasks. It should have a `run` method that takes a task as input and returns a response.
-   `parallel` (bool): If `True`, the tasks will be executed in parallel using a `ThreadPoolExecutor`. Default: `False`.

## Class Methods
-------------

### `add(task: str) -> Task`

Adds a new task to the workflow.

-   `task` (str): The task to be added.

Returns:

-   `Task`: The newly created task object.

### `run(*args) -> Task`

Executes the workflow by running each task in order.

Returns:

-   `Task`: The last task in the workflow.

### `context(task: Task) -> Dict[str, Any]`

Returns a dictionary containing the context information for a given task. The context includes the parent output, parent task, and child task.

-   `task` (Task): The task for which the context information is required.

Returns:

-   `Dict[str, Any]`: A dictionary containing the context information.

## Task Class
----------

The `Task` class is a nested class within the `Workflow` class. It represents an individual task in the workflow.

### Task Parameters

-   `task` (str): The task description.

### Task Methods

### `add_child(child: 'Workflow.Task')`

Adds a child task to the current task.

-   `child` ('Workflow.Task'): The child task to be added.

### `execute() -> Any`

Executes the task by running the associated agent's `run` method with the task as input.

Returns:

-   `Any`: The response from the agent's `run` method.


## Functionality and Usage 
-----------------------------------

To use the `Workflow` class, follow these steps:

1.  Create an instance of the `Workflow` class, providing an agent object that has a `run` method. This agent will be responsible for executing the tasks in the workflow.

```
from swarms import Workflow

# Create an instance of the Workflow class
workflow = Workflow(agent=my_agent)
```


1.  Add tasks to the workflow using the `add` method. Each task should be a string description.

```
# Add tasks to the workflow
task1 = workflow.add("Task 1")
task2 = workflow.add("Task 2")
task3 = workflow.add("Task 3")
```


1.  Define the sequence of tasks by adding child tasks to each task using the `add_child` method.

```
# Define the sequence of tasks
task1.add_child(task2)
task2.add_child(task3)
```


1.  Execute the workflow using the `run` method. This will run each task in order, with the output of each task being passed as input to the next task.

```
# Execute the workflow
workflow.run()
```


1.  Access the output of each task using the `output` attribute of the task object.

```
# Access the output of each task
output1 = task1.output
output2 = task2.output
output3 = task3.output
```


1.  Optionally, you can run the tasks in parallel by setting the `parallel` parameter to `True` when creating the `Workflow` object.

```
# Create a parallel workflow
parallel_workflow = Workflow(agent=my_agent, parallel=True)
```


1.  You can also access the context information for a task using the `context` method. This method returns a dictionary containing the parent output, parent task, and child task for the given task.

```
# Access the context information for a task
context = workflow.context(task2)
parent_output = context["parent_output"]
parent_task = context["parent"]
child_task = context["child"]
```