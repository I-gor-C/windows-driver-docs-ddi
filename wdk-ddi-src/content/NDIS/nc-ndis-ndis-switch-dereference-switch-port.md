---
UID: NC.ndis.NDIS_SWITCH_DEREFERENCE_SWITCH_PORT
title: NDIS_SWITCH_DEREFERENCE_SWITCH_PORT
author: windows-driver-content
description: The DereferenceSwitchPort function decrements the Hyper-V extensible switch reference counter for an extensible switch port. The reference counter was incremented through a previous call to ReferenceSwitchPort.
old-location: netvista\DereferenceSwitchPort.htm
ms.assetid: 976D3A69-C539-4C8E-9664-F85717E5F712
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DereferenceSwitchPort
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# NDIS_SWITCH_DEREFERENCE_SWITCH_PORT callback



## -description
<p>
<p>The <i>DereferenceSwitchPort</i> function decrements the Hyper-V extensible switch reference counter for an extensible switch port. The reference counter was incremented through a previous call to <a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a>.</p>
</p>
<p>The <i>DereferenceSwitchPort</i> function decrements the Hyper-V extensible switch reference counter for an extensible switch port. The reference counter was incremented through a previous call to <a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a>.</p>


## -prototype

````
NDIS_SWITCH_DEREFERENCE_SWITCH_PORT DereferenceSwitchPort;

NDIS_STATUS DereferenceSwitchPort(
  _In_ NDIS_SWITCH_CONTEXT NdisSwitchContext,
  _In_ NDIS_SWITCH_PORT_ID SwitchPortId
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisSwitchContext</i> [in]

<dd>
<p>An NDIS_SWITCH_CONTEXT value that contains the handle of the extensible switch module to which the Hyper-V extensible switch extension is attached. When the extension calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>,  this handle is returned through the <i>NdisSwitchContext</i> parameter.</p>
</dd>

### -param <i>SwitchPortId</i> [in]

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port for which the extensible switch reference counter is incremented.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns NDIS_STATUS_SUCCESS. Otherwise, it returns an NDIS_STATUS_<i>Xxx</i> error code that is defined in Ndis.h.

</p>

## -remarks
<p>The extensible switch extension calls <i>DereferenceSwitchPort</i> to decrement the reference counter for an extensible switch port. While the extensible switch reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a> to delete the port.</p>

<p>The extension must call <i>DereferenceSwitchPort</i> if it had previously called <a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a> for an extensible switch port. </p>

<p>The extensible switch extension calls <i>DereferenceSwitchPort</i> to decrement the reference counter for an extensible switch port. While the extensible switch reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a> to delete the port.</p>

<p>The extension must call <i>DereferenceSwitchPort</i> if it had previously called <a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a> for an extensible switch port. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598204">NdisFGetOptionalSwitchHandlers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598273">OID_SWITCH_PORT_DELETE</a>
</dt>
<dt>
<a href="netvista.ReferenceSwitchPort">ReferenceSwitchPort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_DEREFERENCE_SWITCH_PORT callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
