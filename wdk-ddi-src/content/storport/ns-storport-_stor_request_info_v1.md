---
UID : NS:storport._STOR_REQUEST_INFO_V1
title : _STOR_REQUEST_INFO_V1
author : windows-driver-content
description : The _STOR_REQUEST_INFO_V1 structure contains details about the storage driver IO request associated with a SCSI request block (SRB). _STOR_REQUEST_INFO_V1 is returned by the StorPortGetRequestInfo routine.
old-location : storage\stor_request_info.htm
old-project : storage
ms.assetid : CCC429B7-88BB-4DC3-86BC-6A5FCD405A5D
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STOR_REQUEST_INFO_V1, STOR_REQUEST_INFO_V1, *PSTOR_REQUEST_INFO_V1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : storport.h
req.include-header : Storport.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 8 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STOR_REQUEST_INFO_V1
req.alt-loc : Storport.h
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
req.typenames : STOR_REQUEST_INFO_V1, *PSTOR_REQUEST_INFO_V1
req.product : Windows 10 or later.
---

# _STOR_REQUEST_INFO_V1 structure
The <b>_STOR_REQUEST_INFO_V1</b> structure contains details about the storage driver IO request associated  with a SCSI request block (SRB). <b>_STOR_REQUEST_INFO_V1</b> is returned by the  
  <a href="..\storport\nf-storport-storportgetrequestinfo.md">StorPortGetRequestInfo</a> routine.

## Syntax
````
typedef struct _STOR_REQUEST_INFO_V1 {
  USHORT                Version;
  USHORT                Size;
  STOR_IO_PRIORITY_HINT PriorityHint;
  ULONG                 Flags;
  ULONG                 Key;
  ULONG                 Length;
  BOOLEAN               IsWriteRequest;
  UCHAR                 Reserved[3];
} STOR_REQUEST_INFO_V1, *PSTOR_REQUEST_INFO_V1;
````

## Members

        
            `Flags`

            Flags set for handling the request. May be a combination of these values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `IsWriteRequest`

            True if this is a write request. Otherwise, false, if this is a read request.
        
            `Key`

            The read or write key for the request.
        
            `Length`

            The length of the data in this request.
        
            `PriorityHint`

            The priority hint set for the IO request.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Reserved`

            Reserved.
        
            `Size`

            The size of this structure. Set this value to <b>sizeof</b>(STOR_REQUEST_INFO).
        
            `Version`

            The version of this structure. Set this member to <b>STOR_REQUEST_INFO_VER_1</b>.

    ## Remarks
        The caller to <a href="..\storport\nf-storport-storportgetrequestinfo.md">StorPortGetRequestInfo</a> allocates the <b>STOR_REQUEST_INFO</b> structure. Prior to calling <b>StorPortGetRequestInfo</b>,  <b>Version</b> must be set to <b>STOR_REQUEST_INFO_VER_1</b> and <b>Size</b> must be set to <b>sizeof</b>(STOR_REQUEST_INFO). Otherwise, <b>StorPortGetRequestInfo</b> will return with a status of <b>STOR_STATUS_INVALID_PARAMETER</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |

    ## See Also

        <dl>
<dt>
<a href="..\storport\nf-storport-storportgetrequestinfo.md">StorPortGetRequestInfo</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20_STOR_REQUEST_INFO_V1 structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>