# Declarations in the wdfregistry header
This header Wdfregistry contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFREGISTRYOPENKEY callback function](nc-wdfregistry-pfn-wdfregistryopenkey.md) | TBD |
| [PFN_WDFREGISTRYQUERYSTRING callback function](nc-wdfregistry-pfn-wdfregistryquerystring.md) | TBD |
| [PFN_WDFREGISTRYQUERYVALUE callback function](nc-wdfregistry-pfn-wdfregistryqueryvalue.md) | TBD |
| [PFN_WDFREGISTRYASSIGNMULTISTRING callback function](nc-wdfregistry-pfn-wdfregistryassignmultistring.md) | TBD |
| [PFN_WDFREGISTRYCREATEKEY callback function](nc-wdfregistry-pfn-wdfregistrycreatekey.md) | TBD |
| [PFN_WDFREGISTRYREMOVEVALUE callback function](nc-wdfregistry-pfn-wdfregistryremovevalue.md) | TBD |
| [PFN_WDFREGISTRYASSIGNSTRING callback function](nc-wdfregistry-pfn-wdfregistryassignstring.md) | TBD |
| [PFN_WDFREGISTRYASSIGNVALUE callback function](nc-wdfregistry-pfn-wdfregistryassignvalue.md) | TBD |
| [PFN_WDFREGISTRYASSIGNUNICODESTRING callback function](nc-wdfregistry-pfn-wdfregistryassignunicodestring.md) | TBD |
| [PFN_WDFREGISTRYQUERYMULTISTRING callback function](nc-wdfregistry-pfn-wdfregistryquerymultistring.md) | TBD |
| [PFN_WDFREGISTRYREMOVEKEY callback function](nc-wdfregistry-pfn-wdfregistryremovekey.md) | TBD |
| [PFN_WDFREGISTRYQUERYUNICODESTRING callback function](nc-wdfregistry-pfn-wdfregistryqueryunicodestring.md) | TBD |
| [PFN_WDFREGISTRYQUERYMEMORY callback function](nc-wdfregistry-pfn-wdfregistryquerymemory.md) | TBD |
| [PFN_WDFREGISTRYWDMGETHANDLE callback function](nc-wdfregistry-pfn-wdfregistrywdmgethandle.md) | TBD |
| [PFN_WDFREGISTRYASSIGNMEMORY callback function](nc-wdfregistry-pfn-wdfregistryassignmemory.md) | TBD |
| [PFN_WDFREGISTRYQUERYULONG callback function](nc-wdfregistry-pfn-wdfregistryqueryulong.md) | TBD |
| [PFN_WDFREGISTRYASSIGNULONG callback function](nc-wdfregistry-pfn-wdfregistryassignulong.md) | TBD |
| [PFN_WDFREGISTRYCLOSE callback function](nc-wdfregistry-pfn-wdfregistryclose.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfRegistryAssignMultiString function](nf-wdfregistry-wdfregistryassignmultistring.md) | The WdfRegistryAssignMultiString method assigns a set of strings to a specified value name in the registry. The strings are contained in a specified collection of framework string objects. |
| [WdfRegistryClose function](nf-wdfregistry-wdfregistryclose.md) | The WdfRegistryClose method closes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object. |
| [WdfRegistryRemoveValue function](nf-wdfregistry-wdfregistryremovevalue.md) | The WdfRegistryRemoveValue method removes a specified value and its data from a specified registry key. |
| [WdfRegistryAssignULong function](nf-wdfregistry-wdfregistryassignulong.md) | The WdfRegistryAssignULong method assigns a specified unsigned long word value to a specified value name in the registry. |
| [WdfRegistryAssignValue function](nf-wdfregistry-wdfregistryassignvalue.md) | The WdfRegistryAssignValue method assigns specified data to a specified value name in the registry. |
| [WdfRegistryCreateKey function](nf-wdfregistry-wdfregistrycreatekey.md) | The WdfRegistryCreateKey method creates and opens a specified registry key, or just opens the key if it already exists, and creates a framework registry-key object that represents the registry key. |
| [WdfRegistryQueryULong function](nf-wdfregistry-wdfregistryqueryulong.md) | The WdfRegistryQueryULong method retrieves the unsigned long word (REG_DWORD) data that is currently assigned to a specified registry value and copies the data to a specified location. |
| [WdfRegistryQueryMemory function](nf-wdfregistry-wdfregistryquerymemory.md) | The WdfRegistryQueryMemory method retrieves the data that is currently assigned to a specified registry value, stores the data in a framework-allocated buffer, and creates a framework memory object to represent the buffer. |
| [WdfRegistryQueryString function](nf-wdfregistry-wdfregistryquerystring.md) | The WdfRegistryQueryString method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object. |
| [WdfRegistryAssignUnicodeString function](nf-wdfregistry-wdfregistryassignunicodestring.md) | The WdfRegistryAssignUnicodeString method assigns a specified Unicode string to a specified value name in the registry. |
| [WdfRegistryRemoveKey function](nf-wdfregistry-wdfregistryremovekey.md) | The WdfRegistryRemoveKey method removes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object. |
| [WdfRegistryQueryMultiString function](nf-wdfregistry-wdfregistryquerymultistring.md) | The WdfRegistryQueryMultiString method retrieves the strings that are currently assigned to a specified multi-string registry value, creates a framework string object for each string, and adds each string object to a specified object collection. |
| [WdfRegistryQueryValue function](nf-wdfregistry-wdfregistryqueryvalue.md) | The WdfRegistryQueryValue method retrieves the data that is currently assigned to a specified registry value. |
| [WdfRegistryWdmGetHandle function](nf-wdfregistry-wdfregistrywdmgethandle.md) | The WdfRegistryWdmGetHandle method returns a Windows Driver Model (WDM) handle to the registry key that a specified framework registry-key object represents. |
| [WdfRegistryQueryUnicodeString function](nf-wdfregistry-wdfregistryqueryunicodestring.md) | The WdfRegistryQueryUnicodeString method retrieves the string data that is currently assigned to a specified registry string value and copies the string to a specified UNICODE_STRING structure. |
| [WdfRegistryOpenKey function](nf-wdfregistry-wdfregistryopenkey.md) | The WdfRegistryOpenKey method opens a specified registry key and creates a framework registry-key object that represents the registry key. |
| [WdfRegistryAssignMemory function](nf-wdfregistry-wdfregistryassignmemory.md) | The WdfRegistryAssignMemory method assigns data that is contained in a specified memory buffer to a specified value name in the registry. |
| [WdfRegistryAssignString function](nf-wdfregistry-wdfregistryassignstring.md) | The WdfRegistryAssignString method assigns a string to a specified value name in the registry. The string is contained in a specified framework string object. |

This header is used in these topics:

- [wdf](..content/_wdf)
