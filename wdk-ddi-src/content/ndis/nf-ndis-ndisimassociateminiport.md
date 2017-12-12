---
UID: NF.ndis.NdisIMAssociateMiniport
title: NdisIMAssociateMiniport function
author: windows-driver-content
description: The NdisIMAssociateMiniport function informs NDIS that the specified lower and upper interfaces for miniport and protocol drivers respectively belong to the same intermediate driver.
old-location: netvista\ndisimassociateminiport.htm
old-project: netvista
ms.assetid: b2c46419-644b-4ad4-aa50-7c6e541638aa
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisIMAssociateMiniport
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisIMAssociateMiniport (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisIMAssociateMiniport (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIMAssociateMiniport
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_IM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# NdisIMAssociateMiniport function



## -description
The
  <b>NdisIMAssociateMiniport</b> function informs NDIS that the specified lower and upper interfaces for
  miniport and protocol drivers respectively belong to the same intermediate driver.



## -syntax

````
VOID NdisIMAssociateMiniport(
  _In_ NDIS_HANDLE DriverHandle,
  _In_ NDIS_HANDLE ProtocolHandle
);
````


## -parameters

### -param DriverHandle [in]

The handle to the miniport driver interface that the 
     <a href="netvista.ndismregisterminiportdriver">
     NdisMRegisterMiniportDriver</a> function returns.


### -param ProtocolHandle [in]

The handle to the protocol interface that the 
     <a href="netvista.ndisregisterprotocoldriver">
     NdisRegisterProtocolDriver</a> function returns.


## -returns
None


## -remarks
Any NDIS intermediate driver that exports both 
    <i>MiniportXxx</i> and 
    <i>ProtocolXxx</i> functions calls 
    <b>NdisIMAssociateMiniport</b> to inform the NDIS library about its miniport upper edge and its protocol
    lower edge. Such an intermediate driver calls 
    <b>NdisIMAssociateMiniport</b> during its 
    <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine. For more information about 
    <b>DriverEntry</b>, see 
    <a href="netvista.driverentry_of_ndis_intermediate_drivers">DriverEntry of NDIS
    Intermediate Drivers</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/5c271865-3cc5-47ad-ab58-b5260056a698">NdisIMAssociateMiniport (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisIMAssociateMiniport (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_im_function">Irql_IM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a>
</dt>
<dt>
<a href="netvista.ndismregisterminiportdriver">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="netvista.ndisregisterprotocoldriver">NdisRegisterProtocolDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIMAssociateMiniport function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

