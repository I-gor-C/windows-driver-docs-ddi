---
UID: NS.ucxroothub._ROOTHUB_30PORTS_INFO
title: ROOTHUB_30PORTS_INFO
author: windows-driver-content
description: Provides information about USB 3.0 root hub ports. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_30PORT_INFO callback function.
old-location: buses\_roothub_30ports_info.htm
old-project: usbref
ms.assetid: 2E727D84-193C-45AA-AEC4-75B72BB23FC9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ROOTHUB_30PORTS_INFO, ROOTHUB_30PORTS_INFO, *PROOTHUB_30PORTS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ROOTHUB_30PORTS_INFO
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ROOTHUB_30PORTS_INFO structure



## -description
<p>Provides information about USB 3.0 root hub ports. This structure is passed by UCX in the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-get-30port-info.md">EVT_UCX_ROOTHUB_GET_30PORT_INFO</a> callback function.</p>


## -syntax

````
typedef struct _ROOTHUB_30PORTS_INFO {
  ULONG                 Size;
  USHORT                NumberOfPorts;
  USHORT                PortInfoSize;
   PROOTHUB_30PORT_INFO *PortInfoArray;
} ROOTHUB_30PORTS_INFO, *P_ROOTHUB_30PORTS_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field NumberOfPorts

<dd>
<p>Number of USB 3.0 root hub ports.</p>
</dd>

### -field PortInfoSize

<dd>
<p>The size of the <a href="..\ucxroothub\ns-ucxroothub--roothub-30port-info.md">ROOTHUB_30PORT_INFO</a> array.</p>
</dd>

### -field PortInfoArray

<dd>
<p>A pointer to an array of  <a href="..\ucxroothub\ns-ucxroothub--roothub-30port-info.md">ROOTHUB_30PORT_INFO</a> structures.</p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-get-30port-info.md">EVT_UCX_ROOTHUB_GET_30PORT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20ROOTHUB_30PORTS_INFO structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
