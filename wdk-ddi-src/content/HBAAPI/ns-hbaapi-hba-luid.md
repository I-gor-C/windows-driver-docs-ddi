---
UID: NS.hbaapi.HBA_LUID
title: HBA_LUID
author: windows-driver-content
description: The HBA_LUID structure contains the identification descriptor from the device identification page of the vital products data returned by a SCSI INQUIRY command.
old-location: storage\hba_luid.htm
ms.assetid: af272e27-6cb4-4f87-9c46-512ac80fa310
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_LUID
req.alt-loc: hbaapi.h
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
ms.keywords: HBA_LUID, HBA_LUID, *PHBA_LUID
req.iface: 
---

# HBA_LUID structure



## -description
<p>The HBA_LUID structure contains the identification descriptor from the device identification page of the vital products data returned by a SCSI INQUIRY command.</p>


## -syntax

````
typedef struct HBA_LUID {
  char buffer[256];
} HBA_LUID, *PHBA_LUID;
````


## -struct-fields
<dl>

### -field <b>buffer</b>

<dd>
<p>Contains a buffer that holds the identification descriptor.</p>
</dd>
</dl>

## -remarks
<p>A vendor specific LUID is not guaranteed to be unique or persistent. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556060">HBA_FCPBindingEntry2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556068">HBA_FcpScsiEntryV2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBA_LUID structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
