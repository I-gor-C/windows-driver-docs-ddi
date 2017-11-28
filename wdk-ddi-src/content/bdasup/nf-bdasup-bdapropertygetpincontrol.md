---
UID: NF.bdasup.BdaPropertyGetPinControl
title: BdaPropertyGetPinControl
author: windows-driver-content
description: The BdaPropertyGetPinControl function retrieves either the identifier or type of a pin.
old-location: stream\bdapropertygetpincontrol.htm
old-project: stream
ms.assetid: ab240a95-6308-4953-95f6-9baa280ecf99
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BdaPropertyGetPinControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Desktop
req.target-min-winverclnt: Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BdaPropertyGetPinControl
req.alt-loc: Bdasup.lib,Bdasup.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Bdasup.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BdaPropertyGetPinControl function



## -description
<p>The <b>BdaPropertyGetPinControl</b> function retrieves either the identifier or type of a pin. </p>


## -syntax

````
NTSTATUS BdaPropertyGetPinControl(
  _In_      PIRP        Irp,
  _In_      PKSPROPERTY pKSProperty,
  _Out_opt_ ULONG       *pulProperty
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Points to the IRP for the request to retrieve pin information. The BDA minidriver receives this IRP with either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564348">KSPROPERTY_BDA_PIN_ID</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564350">KSPROPERTY_BDA_PIN_TYPE</a> request.</p>
</dd>

### -param <i>pKSProperty</i> [in]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property and request type of the property request.</p>
</dd>

### -param <i>pulProperty</i> [out, optional]

<dd>
<p>Points to a variable that receives either the identifier or type of a pin. </p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS or an appropriate error code. </p>

## -remarks
<p>A BDA minidriver calls the <b>BdaPropertyGetPinControl</b> function to retrieve either the identifier or type of a pin after the minidriver receives either a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564348">KSPROPERTY_BDA_PIN_ID</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564350">KSPROPERTY_BDA_PIN_TYPE</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566552">KSPROPSETID_BdaPinControl</a> property set. Most BDA minidrivers can define pin-automation tables so that those minidrivers dispatch the <b>BdaPropertyGetPinControl</b> function directly, without intercepting this request using an internal get-handler (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567177">KStrGetPropertyHandler</a>). </p>

<p>A BDA minidriver calls the <b>BdaPropertyGetPinControl</b> function to retrieve either the identifier or type of a pin after the minidriver receives either a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564348">KSPROPERTY_BDA_PIN_ID</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff564350">KSPROPERTY_BDA_PIN_TYPE</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566552">KSPROPSETID_BdaPinControl</a> property set. Most BDA minidrivers can define pin-automation tables so that those minidrivers dispatch the <b>BdaPropertyGetPinControl</b> function directly, without intercepting this request using an internal get-handler (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567177">KStrGetPropertyHandler</a>). </p>

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
<p>Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.h (include Bdasup.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564348">KSPROPERTY_BDA_PIN_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564350">KSPROPERTY_BDA_PIN_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566552">KSPROPSETID_BdaPinControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BdaPropertyGetPinControl function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
