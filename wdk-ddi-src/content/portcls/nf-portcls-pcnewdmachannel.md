---
UID: NF.portcls.PcNewDmaChannel
title: PcNewDmaChannel
author: windows-driver-content
description: The PcNewDmaChannel function creates a new DMA-channel object. This function is obsolete; for more information, see the following comments.
old-location: audio\pcnewdmachannel.htm
old-project: audio
ms.assetid: 4a3a39ac-0db9-48a9-8da6-c2b914fa1de6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcNewDmaChannel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Obsolete. For all new audio drivers, use a IPortWaveXxx::NewXxxDmaChannel method instead. The PortCls system driver implements the PcNewDmaChannel function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewDmaChannel
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcNewDmaChannel function



## -description
<p>The <b>PcNewDmaChannel</b> function creates a new DMA-channel object. This function is obsolete; for more information, see the following comments.</p>


## -syntax

````
NTSTATUS PcNewDmaChannel(
  _Out_    PDMACHANNEL         *OutDmaChannel,
  _In_opt_ PUNKNOWN            OuterUnknown,
  _In_     POOL_TYPE           PoolType,
  _In_     PDEVICE_DESCRIPTION DeviceDescription,
  _In_     PDEVICE_OBJECT      DeviceObject
);
````


## -parameters
<dl>

### -param OutDmaChannel [out]

<dd>
<p>Output pointer for the DMA-channel object created by this function. This parameter points to a caller-allocated pointer variable into which the function outputs a reference to the newly created <a href="..\portcls\nn-portcls-idmachannel.md">IDmaChannel</a> object. Specify a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param OuterUnknown [in, optional]

<dd>
<p>Pointer to the <a href="com.iunknown">IUnknown</a> interface of an object that needs to aggregate the object. Unless aggregation is required, set this parameter to <b>NULL</b>.</p>
</dd>

### -param PoolType [in]

<dd>
<p>Specifies the type of storage pool from which the object is to be allocated. This is a <a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a> enumeration value. Specify a nonpaged pool type for this parameter.</p>
</dd>

### -param DeviceDescription [in]

<dd>
<p>Pointer to a description of the physical device for which the caller is requesting a DMA object. This parameter points to a structure of type <a href="..\wdm\ns-wdm--device-description.md">DEVICE_DESCRIPTION</a>.</p>
</dd>

### -param DeviceObject [in]

<dd>
<p>Pointer to the device object for the physical adapter device. This parameter points to a system structure of type <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>.</p>
</dd>
</dl>

## -returns
<p><b>PcNewDmaChannel</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p><b>PcNewDmaChannel</b> is obsolete. For all new audio drivers, use one of the following IPortWave <i>Xxx</i>::New<i>Xxx</i>DmaChannel methods in place of <b>PcNewDmaChannel</b>:</p>

<p>
<a href="audio.iportwavepci_newmasterdmachannel">IPortWavePci::NewMasterDmaChannel</a>
</p>

<p>
<a href="audio.iportwavecyclic_newmasterdmachannel">IPortWaveCyclic::NewMasterDmaChannel</a>
</p>

<p>
<a href="audio.iportwavecyclic_newslavedmachannel">IPortWaveCyclic::NewSlaveDmaChannel</a>
</p>

<p>For the sake of backward compatibility, the PortCls system driver will continue to support <b>PcNewDmaChannel</b>, and existing drivers can continue to use this function. For more information, see <a href="https://msdn.microsoft.com/0497acff-1e7f-45b9-b5ec-f1783ea7e900">DirectSound Hardware Acceleration in 64-Bit Versions of Windows XP</a>.</p>

<p>Specify the <i>PoolType</i> parameter to be one of the nonpaged pool types defined in the POOL_TYPE enumeration. The DMA-channel object must not reside in paged memory because several of the methods in the <a href="..\portcls\nn-portcls-idmachannel.md">IDmaChannel</a> interface can be called from IRQL DISPATCH_LEVEL.</p>

<p>The <i>OutDmaChannel</i> and <i>OuterUnknown </i>parameters follow the <a href="https://msdn.microsoft.com/e6b19110-37e2-4d23-a528-6393c12ab650">reference-counting conventions for COM objects</a>.</p>

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
<p>Obsolete. For all new audio drivers, use a IPortWaveXxx::NewXxxDmaChannel method instead. The PortCls system driver implements the PcNewDmaChannel function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="..\portcls\nn-portcls-idmachannel.md">IDmaChannel</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--pool-type.md">POOL_TYPE</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-description.md">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewDmaChannel function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
