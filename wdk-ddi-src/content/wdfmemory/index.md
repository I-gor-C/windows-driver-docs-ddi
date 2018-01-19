---
UID : NA:wdfmemory
ms.assetid : abbf138a-21f3-364c-9c5f-ea0dedb411c8
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wdfmemory.h header



wdfmemory.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER](nf-wdfmemory-wdf_memory_descriptor_init_buffer.md) | The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer. |
| [WDF_MEMORY_DESCRIPTOR_INIT_HANDLE](nf-wdfmemory-wdf_memory_descriptor_init_handle.md) | The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object. |
| [WDF_MEMORY_DESCRIPTOR_INIT_MDL](nf-wdfmemory-wdf_memory_descriptor_init_mdl.md) | The WDF_MEMORY_DESCRIPTOR_INIT_MDL function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified memory descriptor list (MDL). |
| [WdfLookasideListCreate](nf-wdfmemory-wdflookasidelistcreate.md) | The WdfLookasideListCreate method creates a lookaside-list object, from which the driver can obtain memory objects. |
| [WdfMemoryAssignBuffer](nf-wdfmemory-wdfmemoryassignbuffer.md) | The WdfMemoryAssignBuffer method assigns a specified buffer to a memory object that a driver created by calling WdfMemoryCreatePreallocated. |
| [WdfMemoryCopyFromBuffer](nf-wdfmemory-wdfmemorycopyfrombuffer.md) | The WdfMemoryCopyFromBuffer method copies the contents of a specified source buffer into a specified memory object's buffer. |
| [WdfMemoryCopyToBuffer](nf-wdfmemory-wdfmemorycopytobuffer.md) | The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer. |
| [WdfMemoryCreate](nf-wdfmemory-wdfmemorycreate.md) | The WdfMemoryCreate method creates a framework memory object and allocates a memory buffer of a specified size. |
| [WdfMemoryCreateFromLookaside](nf-wdfmemory-wdfmemorycreatefromlookaside.md) | The WdfMemoryCreateFromLookaside method creates a framework memory object and obtains a memory buffer from a specified lookaside list. |
| [WdfMemoryCreatePreallocated](nf-wdfmemory-wdfmemorycreatepreallocated.md) | The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer. |
| [WdfMemoryGetBuffer](nf-wdfmemory-wdfmemorygetbuffer.md) | The WdfMemoryGetBuffer method returns a pointer to the buffer that is associated with a specified memory object. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_MEMORY_DESCRIPTOR](ns-wdfmemory-_wdf_memory_descriptor.md) | The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer. |
| [_WDFMEMORY_OFFSET](ns-wdfmemory-_wdfmemory_offset.md) | The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_WDF_MEMORY_DESCRIPTOR_TYPE](ne-wdfmemory-_wdf_memory_descriptor_type.md) | The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify. |