---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvGetCapabilities
title: IWiaMiniDrv::drvGetCapabilities method
author: windows-driver-content
description: The IWiaMiniDrv::drvGetCapabilities method returns an array of events and commands that a device supports.
old-location: image\iwiaminidrv_drvgetcapabilities.htm
old-project: image
ms.assetid: 946a6ea7-5818-4959-adf2-3568c1b64b1a
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IWiaMiniDrv, IWiaMiniDrv interface [Imaging Devices], drvGetCapabilities method, IWiaMiniDrv::drvGetCapabilities, MiniDrv_c88a03f8-d527-47b0-953c-a7bf231c733e.xml, drvGetCapabilities method [Imaging Devices], drvGetCapabilities method [Imaging Devices], IWiaMiniDrv interface, drvGetCapabilities,IWiaMiniDrv.drvGetCapabilities, image.iwiaminidrv_drvgetcapabilities, wiamindr_lh/IWiaMiniDrv::drvGetCapabilities
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wiamindr_lh.h
api_name:
-	IWiaMiniDrv.drvGetCapabilities
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# drvGetCapabilities method
The <b>IWiaMiniDrv::drvGetCapabilities</b> method returns an array of events and commands that a device supports.

## Syntax

````
HRESULT drvGetCapabilities(
  [in]            BYTE            *pWiasContext,
  [in]            LONG            lFlags,
  [out]           LONG            *pcelt,
  [out, optional] WIA_DEV_CAP_DRV **ppCapabilities,
  [out]           LONG            *plDevErrVal
);
````

## Parameters

`__MIDL__IWiaMiniDrv0048`



`__MIDL__IWiaMiniDrv0049`



`__MIDL__IWiaMiniDrv0050`



`__MIDL__IWiaMiniDrv0051`



`__MIDL__IWiaMiniDrv0052`




## Return Value

On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>. 

The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.

## Remarks

The WIA service calls the minidriver method <b>IWiaMiniDrv::drvGetCapabilities</b> to obtain a list of hardware command capabilities and/or device events. In response to this call, a minidriver sets <i>ppCapabilities</i> with the address of an array of pointers to GUID data. Each GUID corresponds to an event notification or a device command supported by the imaging device. When the <i>lFlags</i> parameter is set to WIA_DEVICE_COMMANDS, the array of GUIDs contains device commands. When <i>lFlags</i> is set to WIA_DEVICE_EVENTS, the array of GUIDs contains events. If <i>lFlags</i> is set to WIA_DEVICE_COMMANDS | WIA_DEVICE_EVENTS, the array of GUIDs contains both events and commands, listed in that order.

The <i>Wiadef.h</i> header lists several predefined commands and events.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiaminidrv.md">IWiaMiniDrv</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>



<a href="..\wiamindr_lh\ns-wiamindr_lh-_wia_dev_cap_drv.md">WIA_DEV_CAP_DRV</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvGetCapabilities method%20 RELEASE:%20(2/27/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>