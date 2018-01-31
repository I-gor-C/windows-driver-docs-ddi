---
UID : NN:wudfusb.IWDFUsbInterface
title : IWDFUsbInterface
author : windows-driver-content
description : The IWDFUsbInterface interface exposes a USB interface that a USB device exposes.
old-location : wdf\iwdfusbinterface.htm
old-project : wdf
ms.assetid : 90770016-1267-437e-af70-99741231dc29
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfusbinterface, IWDFUsbInterface interface, IWDFUsbInterface interface, described, IWDFUsbInterface, wudfusb/IWDFUsbInterface, UMDFUSBref_d505d36b-9a59-452d-b35f-ceeff7a0b818.xml, umdf.iwdfusbinterface
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfusb.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.5
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfusb.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product : Windows 10 or later.
---

# IWDFUsbInterface interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


The <b>IWDFUsbInterface</b> interface exposes a USB interface that a USB device exposes.

## Methods

<p>The <b>IWDFUsbInterface</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfusb.IWDFUsbInterface.GetConfiguredSettingIndex](nf-wudfusb-iwdfusbinterface-getconfiguredsettingindex.md) | The GetConfiguredSettingIndex method retrieves the current setting index for a USB interface. |
| [wudfusb.IWDFUsbInterface.GetInterfaceDescriptor](nf-wudfusb-iwdfusbinterface-getinterfacedescriptor.md) | The GetInterfaceDescriptor method retrieves a descriptor for a USB interface. |
| [wudfusb.IWDFUsbInterface.GetInterfaceNumber](nf-wudfusb-iwdfusbinterface-getinterfacenumber.md) | The GetInterfaceNumber method retrieves the index of a USB interface. |
| [wudfusb.IWDFUsbInterface.GetNumEndPoints](nf-wudfusb-iwdfusbinterface-getnumendpoints.md) | The GetNumEndPoints method retrieves the number of endpoints (pipes) on a USB interface. |
| [wudfusb.IWDFUsbInterface.GetWinUsbHandle](nf-wudfusb-iwdfusbinterface-getwinusbhandle.md) | The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a USB interface. |
| [wudfusb.IWDFUsbInterface.RetrieveUsbPipeObject](nf-wudfusb-iwdfusbinterface-retrieveusbpipeobject.md) | The RetrieveUsbPipeObject method retrieves a USB pipe object for the specified pipe index. |
| [wudfusb.IWDFUsbInterface.SelectSetting](nf-wudfusb-iwdfusbinterface-selectsetting.md) | The SelectSetting method selects the specified alternate setting on a USB interface. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfusb.h |
| **DLL** | WUDFx.dll |