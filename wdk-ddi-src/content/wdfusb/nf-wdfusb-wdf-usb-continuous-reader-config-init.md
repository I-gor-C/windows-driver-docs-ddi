---
UID: NF.wdfusb.WDF_USB_CONTINUOUS_READER_CONFIG_INIT
title: WDF_USB_CONTINUOUS_READER_CONFIG_INIT
author: windows-driver-content
description: The WDF_USB_CONTINUOUS_READER_CONFIG_INIT function initializes a WDF_USB_CONTINUOUS_READER_CONFIG structure.
old-location: wdf\wdf_usb_continuous_reader_config_init.htm
old-project: wdf
ms.assetid: d9bf6c47-b7ce-413d-8871-4d9d68e27715
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_USB_CONTINUOUS_READER_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_CONTINUOUS_READER_CONFIG_INIT
req.alt-loc: wdfusb.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_CONTINUOUS_READER_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> function initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure. </p>


## -syntax

````
VOID WDF_USB_CONTINUOUS_READER_CONFIG_INIT(
  _Out_ PWDF_USB_CONTINUOUS_READER_CONFIG     Config,
  _In_  PFN_WDF_USB_READER_COMPLETION_ROUTINE EvtUsbTargetPipeReadComplete,
  _In_  WDFCONTEXT                            EvtUsbTargetPipeReadCompleteContext,
  _In_  size_t                                TransferLength
);
````


## -parameters
<dl>

### -param Config [out]

<dd>
<p>A pointer to a <a href="..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.</p>
</dd>

### -param EvtUsbTargetPipeReadComplete [in]

<dd>
<p>A pointer to the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a> callback function.</p>
</dd>

### -param EvtUsbTargetPipeReadCompleteContext [in]

<dd>
<p>An untyped pointer to driver-defined context information that the framework passes to the driver's <a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a> callback function.</p>
</dd>

### -param TransferLength [in]

<dd>
<p>The maximum length, in bytes, of data that can be received from the device.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> function zeros the specified <a href="..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure and sets the structure's <b>Size</b> member. It also sets the structure's <b>EvtUsbTargetPipeReadComplete</b>, <b>EvtUsbTargetPipeReadCompleteContext</b>, and <b>TransferLength</b> members to the specified values.</p>

<p>  Note that <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> does <i>not</i> set the structure's <b>EvtUsbTargetPipeReadersFailed</b> member.</p>

<p> After calling <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b>, the driver can optionally add a <b>EvtUsbTargetPipeReadersFailed</b> pointer to the <a href="..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.</p>

<p>For a code example that uses <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b>, see <a href="..\wdfusb\nf-wdfusb-wdfusbtargetpipeconfigcontinuousreader.md">WdfUsbTargetPipeConfigContinuousReader</a>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md">EvtUsbTargetPipeReadComplete</a>
</dt>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md">WDF_USB_CONTINUOUS_READER_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_CONTINUOUS_READER_CONFIG_INIT function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
