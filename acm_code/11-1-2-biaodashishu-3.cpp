#include <iostream>
#include <stack>
#include <cstring>
using namespace std;

int prior(char st)
{
    if(st == '*' || st == '/') return 2;
    if(st == '+' || st == '-') return 1;
    return 0;
}

string midToPost(string middata)
{
    stack<char> op;
    string ans;
    for(int i = 0; i < middata.size(); ++i)
    {
        if(middata[i] >= 'a' && middata[i] <= 'z') ans.append(1, middata[i]);
        else if(middata[i] == '(')
        {
            op.push(middata[i]);
        }
        else if(middata[i] == ')')
        {
            while(op.top() != '(') { ans.append(1, op.top()); op.pop();}
            op.pop();
        }
        else if(op.empty()) op.push(middata[i]);
        else if(prior(middata[i]) > prior(op.top())) op.push(middata[i]);
        else if(prior(middata[i]) <= prior(op.top()))
        {
            while(!op.empty() && prior(middata[i]) <= prior(op.top()))
            {
                ans.append(1, op.top());
                op.pop();
            }
            op.push(middata[i]);
        }
    }
    while(!op.empty())
    {
        ans.append(1, op.top());
        op.pop();
    }
    return ans;
}

void display(string data)
{
    cout << data[0];
    for(int i = 1; i < data.size(); ++i)
    {
        cout << " " << data[i];
    }
    cout << endl;
}

struct Node
{
    char data;
    Node *left, *right;
    Node(char c) : data(c), left(NULL), right(NULL){}
};

Node* create_ET(string postdata)
{
    stack<Node*> st;
    Node *temp;
    for(int i = 0; i < postdata.size(); ++i)
    {
        char c = postdata[i];
        if(c == '+' || c == '-' || c == '*' || c == '/')
        {
            temp = new Node(c);
            temp -> right = st.top();
            st.pop();
            temp -> left = st.top();
            st.pop();
            st.push(temp);
        }
        else
        {
            temp = new Node(c);
            st.push(temp);
        }
    }
    return st.top();
}

void postorder(Node *root)
{
    if(root != NULL)
    {
        postorder(root -> left);
        postorder(root -> right);
        cout << root -> data << " ";
    }
}

int main()
{
    string middata, postdata;
    cin >> middata;
    postdata = midToPost(middata);
    display(postdata);
    Node *r = create_ET(postdata);
    postorder(r);
    cout << endl;
    return 0;
}
