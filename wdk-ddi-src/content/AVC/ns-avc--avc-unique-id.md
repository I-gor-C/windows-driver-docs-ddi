---
UID: NS.avc._AVC_UNIQUE_ID
title: AVC_UNIQUE_ID
author: windows-driver-content
description: The AVC_UNIQUE_ID describe the unique ID of the AV/C unit.
old-location: stream\avc_unique_id.htm
ms.assetid: d2a355e2-e5ff-4d20-ae8c-cdee3f5ddb76
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: avc.h
req.include-header: Avc.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVC_UNIQUE_ID
req.alt-loc: avc.h
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
ms.keywords: AVC_UNIQUE_ID, AVC_UNIQUE_ID, *PAVC_UNIQUE_ID
req.iface: 
---

# AVC_UNIQUE_ID structure



## -description
<p>The AVC_UNIQUE_ID describe the unique ID of the AV/C unit.</p>


## -syntax

````
typedef struct _AVC_UNIQUE_ID {
  GUID DeviceID;
} AVC_UNIQUE_ID, *PAVC_UNIQUE_ID;
````


## -struct-fields
<dl>

### -field <b>DeviceID</b>

<dd>
<p>A GUID representing the unit as a whole. All subunits within the same unit share the same GUID. No two units share the same GUID.</p>
</dd>
</dl>

## -remarks
<p>This structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554166">AVC_FUNCTION_GET_UNIQUE_ID</a> function code.</p>

<p>This structure is used only as a member inside the AVC_MULTIFUNC_IRB structure. It is not used by itself.</p>

<p>See <a href="https://msdn.microsoft.com/3b4ec139-ff01-40bd-8e29-92f554180585">How to Use Avc.sys</a> For information about building and sending an AV/C command.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Avc.h (include Avc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554177">AVC_MULTIFUNC_IRB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554145">AVC_FUNCTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554166">AVC_FUNCTION_GET_UNIQUE_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVC_UNIQUE_ID structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
