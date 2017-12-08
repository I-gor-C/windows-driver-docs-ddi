---
UID: NF.ndis.NdisClOpenAddressFamilyEx
title: NdisClOpenAddressFamilyEx function
author: windows-driver-content
description: The NdisClOpenAddressFamilyEx function registers an address family (AF) that is associated with a call manager for a connection-oriented client.
old-location: netvista\ndisclopenaddressfamilyex.htm
old-project: netvista
ms.assetid: 54170917-60b4-4d8f-bf92-df7d7dc0faee
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisClOpenAddressFamilyEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClOpenAddressFamilyEx
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
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

# NdisClOpenAddressFamilyEx function



## -description
The 
  <b>NdisClOpenAddressFamilyEx</b> function registers an address family (AF) that is associated with a call
  manager for a connection-oriented client.


## -syntax

````
NDIS_STATUS NdisClOpenAddressFamilyEx(
  _In_  NDIS_HANDLE        NdisBindingHandle,
  _In_  PCO_ADDRESS_FAMILY AddressFamily,
  _In_  NDIS_HANDLE        ClientAfContext,
  _Out_ PNDIS_HANDLE       NdisAfHandle
);
````


## -parameters

### -param NdisBindingHandle [in]

The handle that 
     <a href="netvista.ndisopenadapterex">NdisOpenAdapterEx</a> returns and that
     identifies the target network interface card (NIC) or the virtual adapter of the next-lower driver that
     the caller is bound to.

### -param AddressFamily [in]

A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545368">CO_ADDRESS_FAMILY</a> structure that describes
     the call manager and AF to be opened. 
     
This pointer is an input parameter to the client's 
     <a href="..\ndis\nc-ndis-protocol_co_af_register_notify.md">
     ProtocolCoAfRegisterNotify</a> function, which calls 
     <b>NdisClOpenAddressFamilyEx</b>.

### -param ClientAfContext [in]

The handle to a caller-supplied resident context area in which the client maintains state for this
     AF after the AF has been opened. NDIS passes this handle back to the client in all subsequent calls
     concerning this AF if the call to 
     <b>NdisClOpenAddressFamilyEx</b> succeeds.

### -param NdisAfHandle [out]

A pointer to a caller-supplied variable in which 
     <b>NdisClOpenAddressFamilyEx</b> returns a handle that represents the newly opened address family.

## -returns
When 
     <b>NdisClOpenAddressFamilyEx</b> returns anything other than NDIS_STATUS_PENDING, the client should make
     an internal call to its 
     <a href="..\ndis\nc-ndis-protocol_cl_open_af_complete_ex.md">
     ProtocolClOpenAfCompleteEx</a> function. Otherwise, NDIS calls the client's 
     <i>ProtocolClOpenAfCompleteEx</i> function when this operation is completed.

## -remarks
A CoNDIS client calls 
    <b>NdisClOpenAddressFamilyEx</b> from its 
    <a href="..\ndis\nc-ndis-protocol_co_af_register_notify.md">
    ProtocolCoAfRegisterNotify</a> function, after the client checks the input buffer that is pointed to by
    the 
    <i>AddressFamily</i> parameter to determine whether the client recognizes the call manager and registered
    addresses. NDIS forwards the client's call of 
    <b>NdisClOpenAddressFamilyEx</b> to the call manager's 
    <a href="..\ndis\nc-ndis-protocol_cm_open_af.md">ProtocolCmOpenAf</a> function, which
    ensures that the client has passed in a valid AF structure.

A successful call to 
    <b>NdisClOpenAddressFamilyEx</b> sets up communication from the client to a call manager. The client can
    then prepare to receive incoming calls by calling the 
    <a href="netvista.ndisclregistersap">NdisClRegisterSap</a> function. The client
    can also set up a virtual connection (VC) by calling the 
    <a href="netvista.ndiscocreatevc">NdisCoCreateVc</a> function so it can make an
    outgoing call by calling the 
    <a href="netvista.ndisclmakecall">NdisClMakeCall</a> function.

If the client's call to 
    <b>NdisClOpenAddressFamilyEx</b> fails, the client should call the 
    <a href="netvista.ndisunbindadapter">NdisUnbindAdapter</a> function to request
    NDIS to release its binding to the underlying miniport adapter. Otherwise, the client must save the
    handle that is returned at the 
    <i>NdisAfHandle</i> parameter. This handle identifies the call manager to which subsequent requests concerning the given address
    family are directed. The client must treat this returned handle as an opaque variable, passing it
    unmodified and uninterpreted in subsequent 
    <b>Ndis<i>Xxx</i></b> function calls.

NDIS passes the pointer from the 
    <i>ClientAfContext</i> parameter to the client's registered 
    <i>ProtocolClXxx</i> functions in all subsequent calls that concern the AF until the client calls 
    <b>NdisClCloseAddressFamily</b> with the same 
    <i>NdisAfHandle</i> . After the AF is closed, the client can release or reuse the storage that it
    allocated at 
    <i>ClientAfContext</i> .

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
Supported in NDIS 6.0 and later.
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
<a href="devtest.ndis_irql_protocol_driver_function">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545368">CO_ADDRESS_FAMILY</a>
</dt>
<dt>
<a href="netvista.ndisallocatefromnpagedlookasidelist">
   NdisAllocateFromNPagedLookasideList</a>
</dt>
<dt>
<a href="netvista.ndisclcloseaddressfamily">NdisClCloseAddressFamily</a>
</dt>
<dt>
<a href="netvista.ndisclmakecall">NdisClMakeCall</a>
</dt>
<dt>
<a href="netvista.ndisclregistersap">NdisClRegisterSap</a>
</dt>
<dt>
<a href="netvista.ndiscocreatevc">NdisCoCreateVc</a>
</dt>
<dt>
<a href="netvista.ndisopenadapterex">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="netvista.ndisunbindadapter">NdisUnbindAdapter</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_open_af_complete_ex.md">ProtocolClOpenAfCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cm_open_af.md">ProtocolCmOpenAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_co_af_register_notify.md">ProtocolCoAfRegisterNotify</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClOpenAddressFamilyEx function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
