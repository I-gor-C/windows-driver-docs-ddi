---
UID: NA:wdfmemory
---

# Wdfmemory.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfmemory.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFMEMORYASSIGNBUFFER function](nc-wdfmemory-pfn_wdfmemoryassignbuffer.md) | The WdfMemoryAssignBuffer method assigns a specified buffer to a memory object that a driver created by calling WdfMemoryCreatePreallocated. |
| [PFN_WDFMEMORYCOPYFROMBUFFER function](nc-wdfmemory-pfn_wdfmemorycopyfrombuffer.md) | The WdfMemoryCopyFromBuffer method copies the contents of a specified source buffer into a specified memory object's buffer. |
| [PFN_WDFMEMORYCOPYTOBUFFER function](nc-wdfmemory-pfn_wdfmemorycopytobuffer.md) | The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer. |
| [PFN_WDFMEMORYCREATEFROMLOOKASIDE function](nc-wdfmemory-pfn_wdfmemorycreatefromlookaside.md) | The WdfMemoryCreateFromLookaside method creates a framework memory object and obtains a memory buffer from a specified lookaside list. |
| [PFN_WDFMEMORYCREATEPREALLOCATED function](nc-wdfmemory-pfn_wdfmemorycreatepreallocated.md) | The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer. |
| [PFN_WDFMEMORYGETBUFFER function](nc-wdfmemory-pfn_wdfmemorygetbuffer.md) | The WdfMemoryGetBuffer method returns a pointer to the buffer that is associated with a specified memory object. |
| [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function](nf-wdfmemory-wdf_memory_descriptor_init_buffer.md) | The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer. |
| [WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function](nf-wdfmemory-wdf_memory_descriptor_init_handle.md) | The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object. |
| [WDF_MEMORY_DESCRIPTOR_INIT_MDL function](nf-wdfmemory-wdf_memory_descriptor_init_mdl.md) | The WDF_MEMORY_DESCRIPTOR_INIT_MDL function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified memory descriptor list (MDL). |
| [WdfLookasideListCreate function](nf-wdfmemory-wdflookasidelistcreate.md) | The WdfLookasideListCreate method creates a lookaside-list object, from which the driver can obtain memory objects. |
| [WdfMemoryAssignBuffer function](nf-wdfmemory-wdfmemoryassignbuffer.md) | The WdfMemoryAssignBuffer method assigns a specified buffer to a memory object that a driver created by calling WdfMemoryCreatePreallocated. |
| [WdfMemoryCopyFromBuffer function](nf-wdfmemory-wdfmemorycopyfrombuffer.md) | The WdfMemoryCopyFromBuffer method copies the contents of a specified source buffer into a specified memory object's buffer. |
| [WdfMemoryCopyToBuffer function](nf-wdfmemory-wdfmemorycopytobuffer.md) | The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer. |
| [WdfMemoryCreate function](nf-wdfmemory-wdfmemorycreate.md) | The WdfMemoryCreate method creates a framework memory object and allocates a memory buffer of a specified size. |
| [WdfMemoryCreateFromLookaside function](nf-wdfmemory-wdfmemorycreatefromlookaside.md) | The WdfMemoryCreateFromLookaside method creates a framework memory object and obtains a memory buffer from a specified lookaside list. |
| [WdfMemoryCreatePreallocated function](nf-wdfmemory-wdfmemorycreatepreallocated.md) | The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer. |
| [WdfMemoryGetBuffer function](nf-wdfmemory-wdfmemorygetbuffer.md) | The WdfMemoryGetBuffer method returns a pointer to the buffer that is associated with a specified memory object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDFMEMORY_OFFSET structure](ns-wdfmemory-_wdfmemory_offset.md) | The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer. |
| [_WDF_MEMORY_DESCRIPTOR structure](ns-wdfmemory-_wdf_memory_descriptor.md) | The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_MEMORY_DESCRIPTOR_TYPE enumeration](ne-wdfmemory-_wdf_memory_descriptor_type.md) | The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify. |
