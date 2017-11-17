# Declarations in the wdfmemory header
This header Wdfmemory contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfMemoryGetBuffer function](nf-wdfmemory-wdfmemorygetbuffer.md) | The WdfMemoryGetBuffer method returns a pointer to the buffer that is associated with a specified memory object. |
| [WdfLookasideListCreate function](nf-wdfmemory-wdflookasidelistcreate.md) | The WdfLookasideListCreate method creates a lookaside-list object, from which the driver can obtain memory objects. |
| [WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function](nf-wdfmemory-wdf-memory-descriptor-init-handle.md) | The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object. |
| [WdfMemoryAssignBuffer function](nf-wdfmemory-wdfmemoryassignbuffer.md) | The WdfMemoryAssignBuffer method assigns a specified buffer to a memory object that a driver created by calling WdfMemoryCreatePreallocated. |
| [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function](nf-wdfmemory-wdf-memory-descriptor-init-buffer.md) | The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer. |
| [WDF_MEMORY_DESCRIPTOR_INIT_MDL function](nf-wdfmemory-wdf-memory-descriptor-init-mdl.md) | The WDF_MEMORY_DESCRIPTOR_INIT_MDL function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified memory descriptor list (MDL). |
| [WdfMemoryCopyFromBuffer function](nf-wdfmemory-wdfmemorycopyfrombuffer.md) | The WdfMemoryCopyFromBuffer method copies the contents of a specified source buffer into a specified memory object's buffer. |
| [WdfMemoryCreateFromLookaside function](nf-wdfmemory-wdfmemorycreatefromlookaside.md) | The WdfMemoryCreateFromLookaside method creates a framework memory object and obtains a memory buffer from a specified lookaside list. |
| [WdfMemoryCopyToBuffer function](nf-wdfmemory-wdfmemorycopytobuffer.md) | The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer. |
| [WdfMemoryCreate function](nf-wdfmemory-wdfmemorycreate.md) | The WdfMemoryCreate method creates a framework memory object and allocates a memory buffer of a specified size. |
| [WdfMemoryCreatePreallocated function](nf-wdfmemory-wdfmemorycreatepreallocated.md) | The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_MEMORY_DESCRIPTOR structure](ns-wdfmemory--wdf-memory-descriptor.md) | The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer. |
| [WDFMEMORY_OFFSET structure](ns-wdfmemory--wdfmemory-offset.md) | The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFMEMORYCREATEPREALLOCATED callback function](nc-wdfmemory-pfn-wdfmemorycreatepreallocated.md) | TBD |
| [PFN_WDFMEMORYGETBUFFER callback function](nc-wdfmemory-pfn-wdfmemorygetbuffer.md) | TBD |
| [PFN_WDFMEMORYCREATEFROMLOOKASIDE callback function](nc-wdfmemory-pfn-wdfmemorycreatefromlookaside.md) | TBD |
| [PFN_WDFMEMORYASSIGNBUFFER callback function](nc-wdfmemory-pfn-wdfmemoryassignbuffer.md) | TBD |
| [PFN_WDFMEMORYCOPYTOBUFFER callback function](nc-wdfmemory-pfn-wdfmemorycopytobuffer.md) | TBD |
| [*PFN_WDFLOOKASIDELISTCREATE callback function](nc-wdfmemory-pfn-wdflookasidelistcreate.md) | TBD |
| [PFN_WDFMEMORYCOPYFROMBUFFER callback function](nc-wdfmemory-pfn-wdfmemorycopyfrombuffer.md) | TBD |
| [*PFN_WDFMEMORYCREATE callback function](nc-wdfmemory-pfn-wdfmemorycreate.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_MEMORY_DESCRIPTOR_TYPE enumeration](ne-wdfmemory--wdf-memory-descriptor-type.md) | The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify. |

This header is used in these topics:

- [wdf](..content/_wdf)
