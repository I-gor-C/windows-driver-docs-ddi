---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvNotifyPnpEvent
title: IWiaMiniDrv::drvNotifyPnpEvent method
author: windows-driver-content
description: The IWiaMiniDrv::drvNotifyPnpEvent method responds to the event received from the WIA service.
old-location: image\iwiaminidrv_drvnotifypnpevent.htm
old-project: Image
ms.assetid: 55d6d93b-c20f-435b-ba99-2df26bd17240
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IWiaMiniDrv, IWiaMiniDrv::drvNotifyPnpEvent, drvNotifyPnpEvent
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
req.alt-api: IWiaMiniDrv.drvNotifyPnpEvent
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
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvNotifyPnpEvent method



## -description
The <b>IWiaMiniDrv::drvNotifyPnpEvent</b> method responds to the event received from the WIA service.



## -syntax

````
HRESULT drvNotifyPnpEvent(
  [in] const GUID  *pEventGuid,
  [in]       BSTR  bstrDeviceID,
  [in]       ULONG ulReserved
);
````


## -parameters

### -param pEventGuid [in]

Points to a GUID identifying the event.


### -param bstrDeviceID [in]

Specifies a string containing the device's unique identifier. 


### -param ulReserved [in]

Is reserved for system use.


## -returns
On success, the method should return S_OK. If the method fails, it should return a standard COM error code.


## -remarks
The WIA service notifies a WIA minidriver of a supported device event by calling the <b>IWiaMiniDrv::drvNotifyPnpEvent</b> method. In this method the minidriver implements the device-specific functionality needed to respond to the event.

If this method is called with *<i>pEventGuid</i> set to WIA_EVENT_CANCEL_IO device event (described in the Microsoft Windows SDK documentation), it should cancel all current I/O operations as soon as possible.


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
Available in Windows Me and in Windows XP and later.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="image.iwiaminidrv_drvgetcapabilities">IWiaMiniDrv::drvGetCapabilities</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20IWiaMiniDrv::drvNotifyPnpEvent method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

