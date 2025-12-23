#include <iostream>
#include <list>
#include <queue>
#include <unordered_map>
using namespace std;

/* ---------- Linked List: Property Listings ---------- */
list<string> properties;

void addProperty(string p) {
    properties.push_back(p);
}

void showProperties() {
    cout << "\nAvailable Properties:\n";
    for (auto p : properties)
        cout << "- " << p << endl;
}

/* ---------- Queue: Client Inquiries ---------- */
queue<string> inquiries;

void addInquiry(string name) {
    inquiries.push(name);
}

void processInquiry() {
    if (!inquiries.empty()) {
        cout << "Processing inquiry of: " << inquiries.front() << endl;
        inquiries.pop();
    } else {
        cout << "No inquiries pending.\n";
    }
}

/* ---------- Hashing: Property ID Search ---------- */
unordered_map<int, string> propertyMap;

void addPropertyID(int id, string details) {
    propertyMap[id] = details;
}

void searchProperty(int id) {
    if (propertyMap.count(id))
        cout << "Property Found: " << propertyMap[id] << endl;
    else
        cout << "Property not found.\n";
}

/* ---------- MAIN ---------- */
int main() {
    cout << "=== Online Real Estate Finder ===\n";

    // Add properties
    addProperty("2BHK Apartment - Chennai");
    addProperty("Villa - Bangalore");
    showProperties();

    // Inquiries
    addInquiry("Client A");
    addInquiry("Client B");
    processInquiry();

    // Property ID Search
    addPropertyID(101, "2BHK Apartment - Chennai");
    addPropertyID(102, "Villa - Bangalore");
    searchProperty(101);

    cout << "\nProject Finished Successfully.\n";
    return 0;
}
