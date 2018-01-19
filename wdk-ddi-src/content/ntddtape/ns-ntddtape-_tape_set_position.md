---
UID : NS:ntddtape._TAPE_SET_POSITION
title : _TAPE_SET_POSITION
author : windows-driver-content
description : The TAPE_SET_POSITION structure is used in conjunction with the IOCTL_TAPE_SET_POSITION request to move the current position on the tape to the specified partition and offset.
old-location : storage\tape_set_position.htm
old-project : storage
ms.assetid : c9f462b2-4b56-4138-a374-9e9d3e1ae295
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _TAPE_SET_POSITION, *PTAPE_SET_POSITION, TAPE_SET_POSITION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddtape.h
req.include-header : Ntddtape.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : TAPE_SET_POSITION
req.alt-loc : ntddtape.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PTAPE_SET_POSITION, TAPE_SET_POSITION"
---

# _TAPE_SET_POSITION structure
The TAPE_SET_POSITION structure is used in conjunction with the <a href="..\ntddtape\ni-ntddtape-ioctl_tape_set_position.md">IOCTL_TAPE_SET_POSITION</a> request to move the current position on the tape to the specified partition and offset.

## Syntax
````
typedef struct _TAPE_SET_POSITION {
  ULONG         Method;
  ULONG         Partition;
  LARGE_INTEGER Offset;
  BOOLEAN       Immediate;
} TAPE_SET_POSITION, *PTAPE_SET_POSITION;
````

## Members

        
            `Immediate`

            When set to <b>TRUE</b>, indicates that the target device should return status immediately. When set to <b>FALSE</b>, indicates that the device should return status after the operation is complete.
        
            `Method`

            Indicates the type of positioning to perform. This member must have one of the following values:
        
            `Offset`

            Specifies an offset whose type depends on the value in <b>Method</b>. If the specified method positions the tape to a block address, <b>Offset</b> specifies the byte offset into the specified partition. If the specified method is to skip blocks, filemarks, or setmarks, <b>Offset</b> specifies the number to skip. If <b>Offset</b> is zero, the tape is positioned at the beginning of the partition.
        
            `Partition`

            Indicates the partition in which to set the tape's position. This member must have one of the following values:

    ## Remarks
        Note that a drive or a tape may not support all <b>Method</b> values.

Partitions are numbered logically from 1 to N. However, a partition number does not imply a physical position on the tape. For example, partition number one might not be at the beginning of the media.

When the offset specifies a number of blocks, filemarks, or setmarks to position over, a positive value N in the offset causes forward positioning over N blocks, filemarks, or setmarks, halting on the end-of-partition or end-of-tape side of the block, filemark, or setmark. A zero value in the offset causes no change of position. A negative value N in the offset causes reverse positioning, toward the beginning of the partition or the tape media, over N blocks, filemarks, or setmarks, halting on the beginning-of-partition side of a block, filemark, or setmark.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddtape.h (include Ntddtape.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddtape\ni-ntddtape-ioctl_tape_set_position.md">IOCTL_TAPE_SET_POSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567954">TapeMiniSetPosition</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_SET_POSITION structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>