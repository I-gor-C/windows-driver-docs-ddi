---
UID : NS:minitape._SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
title : _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
author : windows-driver-content
description : The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode.
old-location : storage\ses_download_microcode_status_descriptor.htm
old-project : storage
ms.assetid : af686e7a-9426-4151-8ac4-d95ae1689b4c
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR, *PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR, SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : minitape.h
req.include-header : Minitape.h, Storport.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 10, version 1709 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
req.alt-loc : scsi.h
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
req.typenames : "*PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR, SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR"
---

# _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure
The <b>SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</b> structure specifies the status and additional status of a download microcode.

## Syntax
````
typedef struct _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR {
  UCHAR  Reserved1;
  UCHAR  SubEnclosureId;
  UCHAR  Status;
  UCHAR  AdditionalStatus;
  UCHAR  MaximumImageSize[4];
  UCHAR  Reserved2[3];
  UCHAR  ExpectedBufferId;
  UCHAR  ExpectedBufferOffset;
} SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR, *PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR;
````

## Members

        
            `AdditionalStatus`

            Provides an additional status value for certain
values of <i>Status</i> .
        
            `ExpectedBufferId`

            Indicates the next value that the
enclosure services process expects in the <i>BufferId</i> field in <a href="https://msdn.microsoft.com/09c2746f-cfe4-41dc-82ce-0b7e0c348897">SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</a>.
        
            `ExpectedBufferOffset`

            Indicates the next value that the
enclosure services process expects in the <i>BufferOffset</i> field in <a href="https://msdn.microsoft.com/09c2746f-cfe4-41dc-82ce-0b7e0c348897">SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</a>. If the enclosure services process accepts arbitrary <i>BufferOffset</i> values, then it shall set <i>ExpectedBufferOffset</i> to 0xFFFFFFFF.
        
            `MaximumImageSize`

            Indicates the maximum size in bytes of the
microcode image that the enclosure services process accepts. The image may be delivered using one or
more <a href="https://msdn.microsoft.com/09c2746f-cfe4-41dc-82ce-0b7e0c348897">SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</a>.
        
            `Reserved1`

            Reserved for future use.
        
            `Reserved2`

            Reserved for future use.
        
            `Status`

            Specifies the status of download microcode
operations for the subenclosure. After reporting a code indicating completion, the
enclosure services process shall set this field to 0x00 and shall
set the <i>AdditionalStatus</i> field to 0x00. Status may can contain one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
        
            `SubEnclosureId`

            Specifies the subenclosure to which the download microcode
status descriptor applies to.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | minitape.h (include Minitape.h, Storport.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/09c2746f-cfe4-41dc-82ce-0b7e0c348897">SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>