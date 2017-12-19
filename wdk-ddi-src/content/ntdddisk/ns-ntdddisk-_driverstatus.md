---
UID: NS.NTDDDISK._DRIVERSTATUS
title: _DRIVERSTATUS
author: windows-driver-content
description: The DRIVERSTATUS structure is used in conjunction with the SENDCMDOUTPARAMS structure and the SMART_SEND_DRIVE_COMMAND request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command.
old-location: storage\driverstatus.htm
old-project: storage
ms.assetid: de97322f-a756-49a8-a6e6-dab42f278388
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DRIVERSTATUS, DRIVERSTATUS, *PDRIVERSTATUS, LPDRIVERSTATUS, PDRIVERSTATUS, *LPDRIVERSTATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRIVERSTATUS
req.alt-loc: ntdddisk.h
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
---

# _DRIVERSTATUS structure



## -description
The DRIVERSTATUS structure is used in conjunction with the <a href="storage.sendcmdoutparams">SENDCMDOUTPARAMS</a> structure and the <a href="storage.smart_send_drive_command">SMART_SEND_DRIVE_COMMAND</a> request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command.



## -syntax

````
typedef struct _DRIVERSTATUS {
  UCHAR bDriverError;
  UCHAR bIDEError;
  UCHAR bReserved[2];
  ULONG dwReserved[2];
} DRIVERSTATUS, *PDRIVERSTATUS, *LPDRIVERSTATUS;
````


## -struct-fields

### -field bDriverError

Error code from driver, or 0 if no error.


### -field bIDEError

Contents of IDE Error register.


### -field bReserved

Reserved. 


### -field dwReserved

Reserved. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.sendcmdoutparams">SENDCMDOUTPARAMS</a>
</dt>
<dt>
<a href="storage.smart_send_drive_command">SMART_SEND_DRIVE_COMMAND</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DRIVERSTATUS structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

