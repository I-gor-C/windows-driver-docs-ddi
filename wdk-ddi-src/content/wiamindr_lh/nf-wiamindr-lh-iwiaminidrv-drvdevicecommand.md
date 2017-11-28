---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvDeviceCommand
title: IWiaMiniDrv::drvDeviceCommand
author: windows-driver-content
description: The IWiaMiniDrv::drvDeviceCommand method issues a command to a WIA device.
old-location: image\iwiaminidrv_drvdevicecommand.htm
old-project: image
ms.assetid: e17c81a6-8c4e-41f0-bd98-f7a9a0f20893
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaMiniDrv, drvDeviceCommand, IWiaMiniDrv::drvDeviceCommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrv.drvDeviceCommand
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrv
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvDeviceCommand method



## -description
<p>The <b>IWiaMiniDrv::drvDeviceCommand</b> method issues a command to a WIA device.</p>


## -syntax

````
HRESULT drvDeviceCommand(
  [in]                  BYTE        *pWiasContext,
  [in]                  LONG        lFlags,
  [in]            const GUID        *plCommand,
  [out, optional]       IWiaDrvItem **ppWiaDrvItem,
  [out]                 LONG        *plDevErrVal
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>lFlags</i> [in]

<dd>
<p>Is currently unused. </p>
</dd>

### -param <i>plCommand</i> [in]

<dd>
<p>Points to a WIA command GUID. </p>
</dd>

### -param <i>ppWiaDrvItem</i> [out, optional]

<dd>
<p>Points to a memory location that can receive a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543896">IWiaDrvItem Interface</a>. See Remarks.</p>
</dd>

### -param <i>plDevErrVal</i> [out]

<dd>
<p>Points to a memory location that will receive a status code for this method. If this method returns S_OK, the value stored will be zero. Otherwise, a minidriver-specific error code will be stored at the location pointed to by this parameter.</p>
</dd>
</dl>

## -returns
<p>On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>. </p>

<p>The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.

</p>

## -remarks
<p>The method <b>IWiaMiniDrv::drvDeviceCommand</b> is called by the WIA service to issue a WIA service or application generated command to the device. The WIA service only calls the <b>IWiaMiniDrv::drvDeviceCommand </b>method for a command that the device can support in the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff543977">IWiaMiniDrv::drvGetCapabilities</a>.</p>

<p>The <i>ppWiaDrvItem</i> parameter should be considered to be optional, since the minidriver does not normally set the memory location it points to. For certain commands, however, the minidriver places the address of a newly created item in the location pointed to by this parameter. For example, if the command to take a picture is issued (<i>plCommand</i> is set to WIA_CMD_TAKE_PICTURE), the device produces a new image, causing the minidriver to create a new item in the driver item tree, and sets *<i>ppWiaDrvItem</i> to the address of the new item. This informs the WIA service that a new item was created.</p>

<p>The minidriver may include a list of custom commands the device can support in the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff543977">IWiaMiniDrv::drvGetCapabilities</a>.</p>

<p>The WIA service does not write any properties before calling this method. If the command relies on property settings, the minidriver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545020">IWiaMiniDrv::drvWriteItemProperties</a> before issuing the command. For example, the command to take a picture, WIA_CMD_TAKE_PICTURE, might rely on shutter speed and aperture settings, which need to be written to the device before the command is issued.</p>

<p>The method <b>IWiaMiniDrv::drvDeviceCommand</b> is called by the WIA service to issue a WIA service or application generated command to the device. The WIA service only calls the <b>IWiaMiniDrv::drvDeviceCommand </b>method for a command that the device can support in the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff543977">IWiaMiniDrv::drvGetCapabilities</a>.</p>

<p>The <i>ppWiaDrvItem</i> parameter should be considered to be optional, since the minidriver does not normally set the memory location it points to. For certain commands, however, the minidriver places the address of a newly created item in the location pointed to by this parameter. For example, if the command to take a picture is issued (<i>plCommand</i> is set to WIA_CMD_TAKE_PICTURE), the device produces a new image, causing the minidriver to create a new item in the driver item tree, and sets *<i>ppWiaDrvItem</i> to the address of the new item. This informs the WIA service that a new item was created.</p>

<p>The minidriver may include a list of custom commands the device can support in the method <a href="https://msdn.microsoft.com/library/windows/hardware/ff543977">IWiaMiniDrv::drvGetCapabilities</a>.</p>

<p>The WIA service does not write any properties before calling this method. If the command relies on property settings, the minidriver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545020">IWiaMiniDrv::drvWriteItemProperties</a> before issuing the command. For example, the command to take a picture, WIA_CMD_TAKE_PICTURE, might rely on shutter speed and aperture settings, which need to be written to the device before the command is issued.</p>

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
<p>Available in Windows Me and in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543977">IWiaMiniDrv::drvGetCapabilities</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545020">IWiaMiniDrv::drvWriteItemProperties</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvDeviceCommand method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
