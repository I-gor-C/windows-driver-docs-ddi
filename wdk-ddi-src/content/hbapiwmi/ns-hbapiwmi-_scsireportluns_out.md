---
UID: NS.HBAPIWMI._SCSIREPORTLUNS_OUT
title: _ScsiReportLuns_OUT
author: windows-driver-content
description: The ScsiReportLuns_OUT structure is used to report the output parameter data of the ScsiReportLuns WMI method to the WMI client.
old-location: storage\scsireportluns_out2.htm
old-project: storage
ms.assetid: 93663b88-e750-4280-b5c1-798cc0f848b7
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _ScsiReportLuns_OUT, PScsiReportLuns_OUT, *PScsiReportLuns_OUT, ScsiReportLuns_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiReportLuns_OUT
req.alt-loc: Hbapiwmi.h
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

# _ScsiReportLuns_OUT structure



## -description
The ScsiReportLuns_OUT structure is used to report the output parameter data of the <a href="storage.scsireportluns">ScsiReportLuns</a> WMI method to the WMI client.



## -syntax

````
typedef struct _ScsiReportLuns_OUT {
  ULONG HBAStatus;
  ULONG ResponseBufferSize;
  ULONG SenseBufferSize;
  UCHAR ScsiStatus;
  UCHAR ResponseBuffer[1];
  UCHAR SenseBuffer[1];
} ScsiReportLuns_OUT, *PScsiReportLuns_OUT;
````


## -struct-fields

### -field HBAStatus

Contains a value associated with the WMI class qualifier <a href="storage.hba_status">HBA_STATUS</a> that indicates the result of an HBA query operation. 


### -field ResponseBufferSize

Indicates the size in bytes of the buffer that will hold the results of the inquiry command. 


### -field SenseBufferSize

Indicates the size in bytes of the buffer that will hold the SCSI sense data that results from the inquiry command. 


### -field ScsiStatus

Contains the status of the SCSI report LUNs command. 


### -field ResponseBuffer

Contains the results of the SCSI report LUNs command. 


### -field SenseBuffer

Contains the SCSI sense data that results from the SCSI report LUNs command. 


## -remarks
The WMI tool suite generates a declaration of the ScsiReportLuns_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
<dt>
<a href="storage.scsireportluns">ScsiReportLuns</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiReportLuns_OUT structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

