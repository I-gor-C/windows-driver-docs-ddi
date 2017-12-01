---
UID: NF.portcls.IPinName.GetPinName
title: IPinName::GetPinName
author: windows-driver-content
description: The GetPinName method retrieves the friendly name of an audio endpoint.
old-location: audio\ipinname_getpinname.htm
old-project: audio
ms.assetid: 97fa159c-ce71-4ce2-8d40-def7671d014c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPinName, GetPinName, IPinName::GetPinName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPinName.GetPinName
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: IPinName
---

# IPinName::GetPinName method



## -description
<p>The <code>GetPinName</code> method retrieves the friendly name of an audio endpoint.</p>


## -syntax

````
NTSTATUS GetPinName(
  [in]  PIRP     Irp,
  [in]  PKSP_PIN Pin,
  [out] PVOID    Data
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies a pointer to an I/O request packet (IRP) structure. </p>
</dd>

### -param <i>Pin</i> [in]

<dd>
<p>Specifies a pointer to the underlying kernel streaming (KS) pin.</p>
</dd>

### -param <i>Data</i> [out]

<dd>
<p>Specifies a pointer to the buffer that holds the data for the <code>GetPinName</code> method.</p>
</dd>
</dl>

## -returns
<p>The <code>GetPinName</code> method returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>If a client needs the current pin name of an endpoint, but has determined that the miniport driver does not support the <code>GetPinName</code> method, the client uses the friendly name of the topology bridge pin. For more information about pin categories and friendly names, see <a href="NULL">Pin Category Property</a> and <a href="NULL">Friendly Names for Audio Endpoint Devices</a>. </p>

<p>KSNODETYPE_SPEAKER</p>

<p>KSNODETYPE_DESKTOP_SPEAKER</p>

<p>KSNODETYPE_ROOM_SPEAKER</p>

<p>KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-ipinname.md">IPinName</a>
</dt>
<dt>
<a href="NULL">Friendly Names for Audio Endpoint Devices</a>
</dt>
<dt>
<a href="NULL">Pin Category Property</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPinName::GetPinName method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
