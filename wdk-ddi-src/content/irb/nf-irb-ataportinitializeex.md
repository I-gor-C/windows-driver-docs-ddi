---
UID: NF.irb.AtaPortInitializeEx
title: AtaPortInitializeEx
author: windows-driver-content
description: The AtaPortInitializeEx ATA port driver library routine initializes the port and miniport drivers.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportinitializeex.htm
old-project: storage
ms.assetid: 578992cf-63eb-4b8e-b0cb-9caee5c534e1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortInitializeEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortInitializeEx
req.alt-loc: Pciidex.lib,Pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Pciidex.lib
req.dll: 
req.irql: 
req.iface: 
---

# AtaPortInitializeEx function



## -description
<p>The <b>AtaPortInitializeEx</b> ATA port driver library routine initializes the port and miniport drivers.</p>


## -syntax

````
ULONG AtaPortInitializeEx(
  _In_ PVOID                     DriverObject,
  _In_ PVOID                     RegistryPath,
  _In_ PIDE_CONTROLLER_INTERFACE ControllerInterface
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to the miniport driver object.</p>
</dd>

### -param <i>RegistryPath</i> [in]

<dd>
<p>Contains a Unicode string that indicates the location in the registry where the miniport driver configuration information is stored.</p>
</dd>

### -param <i>ControllerInterface</i> [in]

<dd>
<p>Contains the entry points for the <b><i>AtaAdapterControl</i></b>, <b><i>AtaChannelInitRoutine</i></b>, <b><i>AtaControllerChannelEnabled</i></b>, and <b><i>AtaControllerTransferModeSelect</i></b> routines.</p>
</dd>
</dl>

## -returns
<p><b>AtaPortInitializeEx</b> returns STATUS_SUCCESS if the operation succeeds.  Otherwise, it returns an error code. </p>

## -remarks
<p>The <b>AtaPortInitializeEx</b> routine initializes key data structures that are used by the port and miniport drivers. It also starts the initialization of the controller's channels. The following sequence describes the principal actions taken by this routine:</p>

<p>While starting the adapter device, the miniport driver routine <b><i>AtaAdapterControl</i></b> will be called by the port driver with control action <b>IdeStart</b>.</p>

<p>When the ATA port driver is processing a channel device start request, the miniport driver routine <a href="storage.atacontrollerchannelenabled">AtaControllerChannelEnabled</a> is called for each channel on the controller to determine whether it is enabled.</p>

<p>After the <a href="storage.atacontrollerchannelenabled">AtaControllerChannelEnabled</a> routine determines which channels are enabled, the ATA port driver calls <a href="storage.atachannelinitroutine">AtaChannelInitRoutine</a> for this channel. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Pciidex.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.atachannelinitroutine">AtaChannelInitRoutine</a>
</dt>
<dt>
<a href="storage.atacontrollerchannelenabled">AtaControllerChannelEnabled</a>
</dt>
<dt>
<a href="storage.driverentry">DriverEntry</a>
</dt>
<dt>
<a href="..\irb\ns-irb--ide-controller-configuration.md">IDE_CONTROLLER_CONFIGURATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortInitializeEx routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
