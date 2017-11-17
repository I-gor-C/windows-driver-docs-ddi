---
UID: NS.61883._CMP_DELETE_PLUG
title: CMP_DELETE_PLUG
author: windows-driver-content
description: This structure is used to create a plug.
old-location: ieee\cmp_delete_plug.htm
ms.assetid: 93F81B97-5C37-47BF-8867-0FBEFA8F6D3B
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CMP_DELETE_PLUG
req.alt-loc: 61883.h
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
ms.keywords: CMP_DELETE_PLUG, CMP_DELETE_PLUG, *PCMP_DELETE_PLUG
---

# CMP_DELETE_PLUG structure



## -description
<p>This structure is used to create a plug.</p>


## -syntax

````
typedef struct _CMP_DELETE_PLUG {
  HANDLE hPlug;
} CMP_DELETE_PLUG, *PCMP_DELETE_PLUG;
````


## -struct-fields
<dl>

### -field <b><b>hPlug</b></b>

<dd>
<p>A handle to the plug to delete.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CMP_DELETE_PLUG structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
