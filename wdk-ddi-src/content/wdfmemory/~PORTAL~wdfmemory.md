# Wdfmemory.h header


This header is used by unknown technology.

Wdfmemory.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function](nf-wdfmemory-wdf-memory-descriptor-init-buffer.md) | The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer. |
| [WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function](nf-wdfmemory-wdf-memory-descriptor-init-handle.md) | The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object. |
| [WDF_MEMORY_DESCRIPTOR_INIT_MDL function](nf-wdfmemory-wdf-memory-descriptor-init-mdl.md) | The WDF_MEMORY_DESCRIPTOR_INIT_MDL function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified memory descriptor list (MDL). |
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
| [WDFMEMORY_OFFSET structure](ns-wdfmemory--wdfmemory-offset.md) | The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer. |
| [WDF_MEMORY_DESCRIPTOR structure](ns-wdfmemory--wdf-memory-descriptor.md) | The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDF_MEMORY_DESCRIPTOR_TYPE enumeration](ne-wdfmemory--wdf-memory-descriptor-type.md) | The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify. |
