---
UID: NF.ks.KsRegisterFilterWithNoKSPins
title: KsRegisterFilterWithNoKSPins function
author: windows-driver-content
description: The KsRegisterFilterWithNoKSPins function registers with DirectShow filters that have no kernel streaming pins and, therefore, do not stream in kernel mode.
old-location: stream\ksregisterfilterwithnokspins.htm
old-project: stream
ms.assetid: 4ad768c9-211d-4370-b6d3-6d88b223fe48
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KsRegisterFilterWithNoKSPins
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
req.alt-api: KsRegisterFilterWithNoKSPins
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
---

# KsRegisterFilterWithNoKSPins function



## -description
The<b> KsRegisterFilterWithNoKSPins </b>function registers with DirectShow filters that have no kernel streaming pins and, therefore, do not stream in kernel mode.



## -syntax

````
NTSTATUS KsRegisterFilterWithNoKSPins(
  _In_           PDEVICE_OBJECT DeviceObject,
  _In_     const GUID           *InterfaceClassGUID,
  _In_           ULONG          PinCount,
  _In_           BOOL           *PinDirection,
  _In_           KSPIN_MEDIUM   *MediumList,
  _In_opt_       GUID           *CategoryList
);
````


## -parameters

### -param DeviceObject [in]

A pointer to a <a href="kernel.device_object">DEVICE_OBJECT</a> structure corresponding to the device to which to register the filter.


### -param InterfaceClassGUID [in]

A pointer to the GUID representing the class to register. For instance, this would point to KSCATEGORY_TVTUNER for a TvTuner filter.


### -param PinCount [in]

The count of the number of pins on the filter.


### -param PinDirection [in]

A pointer to the first element of an array of Boolean values indicating pin direction for each pin on the filter. Output pins are <b>TRUE</b>; input pins are <b>FALSE</b>. This array must be <i>PinCount</i> in length.


### -param MediumList [in]

A pointer to the first element of an array of <a href="stream.kspin_medium">KSPIN_MEDIUM</a> structures defining the mediums for each pin on the filter. This array must be <i>PinCount</i> in length.


### -param CategoryList [in, optional]

A pointer to the first element of an array of GUIDs defining the categories for each pin on the filter. If this parameter is present, it must be <i>PinCount</i> in length.


## -returns
Returns success or failure of creating the FilterData key in the registry.


## -remarks
Use<b> KsRegisterFilterWithNoKSPins</b> to register TvTuners, Crossbars, and similar components. <b>KsRegisterFilterWithNoKSPins</b> creates a new registry key, <b>FilterData</b>, that contains the mediums, and optionally the categories, for each pin on the filter.

This function is only used to register filters that have no corresponding kernel pins. If successful, <b>KsRegisterFilterWithNoKSPins</b> creates a key in the registry that can be then used by DirectShow.

If writing a BDA minidriver, consider using <a href="stream.ksfilterfactoryupdatecachedata">KsFilterFactoryUpdateCacheData</a> instead of this routine. See details on the reference page for <b>KsFilterFactoryUpdateCacheData</b>.

For more information, see <a href="https://msdn.microsoft.com/fd436406-311b-4537-994d-fbd8d92d4673">AVStream Descriptors</a> and <a href="https://msdn.microsoft.com/666d6efb-93ec-43f3-87c5-ea1a3983bfd0">Initializing an AVStream Minidriver</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksfilterregisterpowercallbacks">KsFilterRegisterPowerCallbacks</a>
</dt>
<dt>
<a href="stream.ksfilterfactoryupdatecachedata">KsFilterFactoryUpdateCacheData</a>
</dt>
<dt>
<a href="kernel.driver_object">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsRegisterFilterWithNoKSPins function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

