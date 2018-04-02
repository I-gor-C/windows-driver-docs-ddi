---
UID: NF:fwpsk.FwpsInjectvSwitchEthernetIngressAsync0
title: FwpsInjectvSwitchEthernetIngressAsync0 function
author: windows-driver-content
description: The FwpsInjectvSwitchEthernetIngressAsync0 (was FwpsInjectvSwitchIngressAsync0) function reinjects a previously absorbed virtual switch packet (unmodified) back to the virtual switch ingress data path where it was intercepted.
old-location: netvista\fwpsinjectvswitchingressasync0.htm
old-project: netvista
ms.assetid: ccb22035-08fe-44a6-88d5-bf9db7c2f499
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: FwpsInjectvSwitchEthernetIngressAsync0, FwpsInjectvSwitchEthernetIngressAsync0 function [Network Drivers Starting with Windows Vista], fwpsk/FwpsInjectvSwitchEthernetIngressAsync0, netvista.fwpsinjectvswitchingressasync0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	fwpkclnt.lib
-	fwpkclnt.dll
api_name:
-	FwpsInjectvSwitchEthernetIngressAsync0
product: Windows
targetos: Windows
req.typenames: FWPS_VSWITCH_EVENT_TYPE
---


# FwpsInjectvSwitchEthernetIngressAsync0 function
The <b>FwpsInjectvSwitchEthernetIngressAsync0</b> (was <b>FwpsInjectvSwitchIngressAsync0</b>) function reinjects a previously absorbed virtual switch packet (unmodified) back to the virtual switch ingress data path where it was intercepted. This function can also inject a packet created with  the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a>  function.
<div class="alert"><b>Note</b>  <b>FwpsInjectvSwitchEthernetIngressAsync0</b> is a specific version of <b>FwpsInjectvSwitchEthernetIngressAsync</b>. See <a href="https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div><div> </div>

## Syntax

```
NTSTATUS FwpsInjectvSwitchEthernetIngressAsync0(
  HANDLE                injectionHandle,
  HANDLE                injectionContext,
  UINT32                flags,
  void                  *reserved,
  const FWP_BYTE_BLOB   *vSwitchId,
  NDIS_SWITCH_PORT_ID   vSwitchSourcePortId,
  NDIS_SWITCH_NIC_INDEX vSwitchSourceNicIndex,
  NET_BUFFER_LIST       *netBufferLists,
  FWPS_INJECT_COMPLETE  completionFn,
  HANDLE                completionContext
);
```

## Parameters

`injectionHandle`

An injection handle that was previously created by a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a> function with the <i>flags</i> parameter set to <b>FWPS_INJECTION_TYPE_VSWITCH</b>.


The <i>addressFamily</i> parameter is not used and should be set to <b>AF_UNSPEC</b>.

`injectionContext`

An optional handle to the injection context that can be  retrieved with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function.

`flags`

Reserved. Must be set to zero.

`reserved`

Reserved. Must be set to NULL.

`vSwitchId`

The virtual  switch identifier that the filtering engine passed in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a> structure to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. This is the  <b>GUID</b> of the virtual switch that is provided in an xxx_VSWITCH_ID field.

`vSwitchSourcePortId`

The virtual  switch source port identifier.

`vSwitchSourceNicIndex`

The virtual  switch source NIC  index.

`netBufferLists`

A chain of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures to be injected into the virtual switch egress data path.

`completionFn`

A pointer to a 
     <a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a> callout function that is provided by
     the callout driver. The filter engine calls this function after the packet data, at the 
     <i>netBufferLists</i> parameter, has been injected into the virtual switch egress data path. The 
     <i>completionFn</i> function will be called once for each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> in the chain. <i>completionFn</i> must be specified when injecting cloned or created <b>NET_BUFFER_LIST</b> structures. This parameter can be NULL when injecting original unaltered <b>NET_BUFFER_LIST</b> structures that were received from the filter engine.

`completionContext`

A pointer to a callout driver–provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.


## Return Value

The 
     <b>FwpsInjectvSwitchEthernetIngressAsync0</b> function returns one of the following <b>NTSTATUS</b> codes.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The virtual switch <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> chain was successfully injected.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred.

</td>
</tr>
</table>

## Remarks

When a callout injects packets with <b>FwpsInjectvSwitchEthernetIngressAsync0</b>, the injected packets could be classified again if the packets match the same filter as they were originally classified. Therefore, like callouts at IP layers, virtual switch callouts must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function to protect against infinite packet inspections.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | fwpsk.h (include Fwpsk.h) |
| **Library** | Fwpkclnt.lib |
| **IRQL** | "<= DISPATCH_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a>