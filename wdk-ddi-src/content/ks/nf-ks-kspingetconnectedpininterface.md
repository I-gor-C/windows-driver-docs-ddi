---
UID: NF.ks.KsPinGetConnectedPinInterface
title: KsPinGetConnectedPinInterface
author: windows-driver-content
description: The KsPinGetConnectedPinInterface function queries the pin to which Pin is connected for a COM style interface.
old-location: stream\kspingetconnectedpininterface.htm
old-project: stream
ms.assetid: 594614ee-0d30-4574-81ad-a523e7fadc2c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinGetConnectedPinInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGetConnectedPinInterface
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsPinGetConnectedPinInterface function



## -description
<p>The<b> KsPinGetConnectedPinInterface</b> function queries the pin to which <i>Pin</i> is connected for a COM style interface.</p>


## -syntax

````
NTSTATUS KsPinGetConnectedPinInterface(
  _In_        PKSPIN Pin,
  _In_  const GUID   *InterfaceId,
  _Out_       PVOID  *Interface
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure. AVStream queries the pin connected to <i>Pin</i> for the requested interface.</p>
</dd>

### -param <i>InterfaceId</i> [in]

<dd>
<p>A pointer to the GUID specifying the interface type to be obtained. A <b>QueryInterface</b> call is automatically performed for this interface.</p>
</dd>

### -param <i>Interface</i> [out]

<dd>
<p>A pointer to a pointer that AVStream sets to the location of the COM interface.</p>
</dd>
</dl>

## -returns
<p><b>KsPinGetConnectedPinInterface</b> returns STATUS_SUCCESS or STATUS_NOINTERFACE. See details below.</p>

## -remarks
<p><i>Interface</i> has a corresponding reference count and <b>must</b> be released by the caller as in COM.</p>

<p>This routine returns STATUS_SUCCESS if the interface exists on the connected pin or in the AVStream thunk. If STATUS_SUCCESS is returned, AVStream deposits the interface pointer into <i>*Interface</i>. Otherwise, the routine returns STATUS_NOINTERFACE. This corresponds to the COM HRESULT E_NOINTERFACE.</p>

<p>By default, objects support the <b>IUnknown</b> interface and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559766">IKsControl</a> interface. If the connected pin is an AVStream pin, the query and the returned interface pointer are direct calls to the other driver. If, on the other hand, the connected pin does not belong to an AVStream driver, a thunk is created that provides <i>IKsControl </i>support through synchronous calls to the driver containing the connected pin, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>.</p>

<p>The most common usage of <b>KsPinGetConnectedPinInterface</b> is to acquire the control interface for the connected pin. This control interface can be used for property, method, or event calls down to the connected pin or can query for interfaces that have been aggregated onto the connected pin. If the connected pin is an AVStream pin; AVStream only provides thunking for <b>IKsControl</b> and <b>IUnknown</b> for non-AVStream pins.</p>

<p>The thunk is only created if<i> Pin</i> is a source pin; thus, the calls only work if one or more of the following is true:</p>

<p>The connection is intra-AVStream (<i>Pin</i>'s connected pin is an AVStream pin).</p>

<p><i>Pin</i> is a source pin.</p>

<p>Otherwise, STATUS_UNSUCCESSFUL is returned.</p>

<p><i>Interface</i> has a corresponding reference count and <b>must</b> be released by the caller as in COM.</p>

<p>This routine returns STATUS_SUCCESS if the interface exists on the connected pin or in the AVStream thunk. If STATUS_SUCCESS is returned, AVStream deposits the interface pointer into <i>*Interface</i>. Otherwise, the routine returns STATUS_NOINTERFACE. This corresponds to the COM HRESULT E_NOINTERFACE.</p>

<p>By default, objects support the <b>IUnknown</b> interface and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559766">IKsControl</a> interface. If the connected pin is an AVStream pin, the query and the returned interface pointer are direct calls to the other driver. If, on the other hand, the connected pin does not belong to an AVStream driver, a thunk is created that provides <i>IKsControl </i>support through synchronous calls to the driver containing the connected pin, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>.</p>

<p>The most common usage of <b>KsPinGetConnectedPinInterface</b> is to acquire the control interface for the connected pin. This control interface can be used for property, method, or event calls down to the connected pin or can query for interfaces that have been aggregated onto the connected pin. If the connected pin is an AVStream pin; AVStream only provides thunking for <b>IKsControl</b> and <b>IUnknown</b> for non-AVStream pins.</p>

<p>The thunk is only created if<i> Pin</i> is a source pin; thus, the calls only work if one or more of the following is true:</p>

<p>The connection is intra-AVStream (<i>Pin</i>'s connected pin is an AVStream pin).</p>

<p><i>Pin</i> is a source pin.</p>

<p>Otherwise, STATUS_UNSUCCESSFUL is returned.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563506">KsPinGetConnectedFilterInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563517">KsPinGetReferenceClockInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562655">KsGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559766">IKsControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560725">IKsReferenceClock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562547">KsFilterGetOuterUnknown</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566767">KsRegisterAggregatedClientUnknown</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetConnectedPinInterface function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
