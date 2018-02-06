---
UID: NS:spb.SPB_TRANSFER_BUFFER
title: SPB_TRANSFER_BUFFER
author: windows-driver-content
description: The SPB_TRANSFER_BUFFER structure describes the data buffer for an individual transfer in an I/O transfer sequence.
old-location: spb\spb_transfer_buffer.htm
old-project: SPB
ms.assetid: E9C5B866-1EB0-4043-B22F-DF2F4CFAE64C
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: "*PSPB_TRANSFER_BUFFER, PSPB_TRANSFER_BUFFER structure pointer [Buses], spb/PSPB_TRANSFER_BUFFER, spb/SPB_TRANSFER_BUFFER, SPB.spb_transfer_buffer, PSPB_TRANSFER_BUFFER, SPB_TRANSFER_BUFFER, SPB_TRANSFER_BUFFER structure [Buses]"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: spb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Spb.h
apiname:
-	SPB_TRANSFER_BUFFER
product: Windows
targetos: Windows
req.typenames: "*PSPB_TRANSFER_BUFFER, SPB_TRANSFER_BUFFER"
req.product: Windows 10 or later.
---

# SPB_TRANSFER_BUFFER structure
The <b>SPB_TRANSFER_BUFFER</b> structure describes the data buffer for an individual transfer in an <a href="https://msdn.microsoft.com/7415DB28-5E93-4F47-B169-7C652969D4C7">I/O transfer sequence</a>.

## Syntax
````
typedef struct _SPB_TRANSFER_BUFFER {
  SPB_TRANSFER_BUFFER_FORMAT Format;
  union {
    SPB_TRANSFER_BUFFER_LIST_ENTRY Simple;
    struct {
      PSPB_TRANSFER_BUFFER_LIST_ENTRY List;
      ULONG                           ListCe;
    } BufferList;
    PMDL                           Mdl;
  };
} SPB_TRANSFER_BUFFER, *PSPB_TRANSFER_BUFFER;
````

## Members


`Format`

The buffer format.  This member is set to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/hh406216">SPB_TRANSFER_BUFFER_FORMAT</a> enumeration values:
<ul>
<li><b>SpbTransferBufferFormatSimple</b></li>
<li><b>SpbTransferBufferFormatList</b></li>
<li><b>SpbTransferBufferFormatSimpleNonPaged</b></li>
<li><b>SpbTransferBufferFormatMdl</b></li>
</ul><b>SpbTransferBufferFormatMdl</b> is a valid value only for I/O transfer sequences that are requested by clients of the SPB controller driver that are kernel-mode components.

## Remarks
This structure is used by an <a href="https://msdn.microsoft.com/library/windows/hardware/hh406223">SPB_TRANSFER_LIST_ENTRY</a> structure to describe a transfer buffer.

The <b>Mdl</b> member of this structure can be used only by clients of the SPB controller driver that are kernel-mode components. User-mode clients must not use this member. For more information about MDLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | spb.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406217">SPB_TRANSFER_BUFFER_LIST_ENTRY</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406216">SPB_TRANSFER_BUFFER_FORMAT</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406223">SPB_TRANSFER_LIST_ENTRY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SPB_TRANSFER_BUFFER structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>