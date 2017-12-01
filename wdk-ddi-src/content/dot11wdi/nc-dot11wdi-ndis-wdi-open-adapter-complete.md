---
UID: NC.dot11wdi.NDIS_WDI_OPEN_ADAPTER_COMPLETE
title: NDIS_WDI_OPEN_ADAPTER_COMPLETE
author: windows-driver-content
description: The NdisWdiOpenAdapterComplete callback function is called by the IHV when an Open Task operation from MiniportWdiOpenAdapter has been successfully started.
old-location: netvista\ndiswdiopenadaptercomplete.htm
old-project: netvista
ms.assetid: FD6FF134-A8D7-433E-9353-88965E67749E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWdiOpenAdapterComplete
req.alt-loc: dot11wdi.h
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
req.iface: ISynthSinkDMus
---

# NDIS_WDI_OPEN_ADAPTER_COMPLETE callback



## -description
<p>The NdisWdiOpenAdapterComplete callback function is called by the IHV when an Open Task operation from <a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-open-adapter.md">MiniportWdiOpenAdapter</a> has been successfully started.</p>
<p>This is a control path callback inside <a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-init-parameters.md">NDIS_WDI_INIT_PARAMETERS</a>.</p>


## -prototype

````
NDIS_WDI_OPEN_ADAPTER_COMPLETE NdisWdiOpenAdapterComplete;

VOID NdisWdiOpenAdapterComplete(
  _In_ NDIS_HANDLE MiniportAdapterHandle,
  _In_ NDIS_STATUS CompletionStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport handle.</p>
</dd>

### -param <i>CompletionStatus</i> [in]

<dd>
<p>The completion status.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dot11wdi\nc-dot11wdi-miniport-wdi-open-adapter.md">MiniportWdiOpenAdapter</a>
</dt>
<dt>
<a href="..\dot11wdi\ns-dot11wdi--ndis-wdi-init-parameters.md">NDIS_WDI_INIT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WDI_OPEN_ADAPTER_COMPLETE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
