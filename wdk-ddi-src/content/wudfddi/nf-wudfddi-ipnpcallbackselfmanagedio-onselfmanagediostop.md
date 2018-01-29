---
UID : NF:wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoStop
title : IPnpCallbackSelfManagedIo::OnSelfManagedIoStop method
author : windows-driver-content
description : The OnSelfManagedIoStop method is not used in the current version of the UMDF.
old-location : wdf\ipnpcallbackselfmanagedio_onselfmanagediostop.htm
old-project : wdf
ms.assetid : 490c95f5-ea93-4521-8fa5-4ca1f83ff19d
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : OnSelfManagedIoStop method, IPnpCallbackSelfManagedIo interface, IPnpCallbackSelfManagedIo, OnSelfManagedIoStop method, OnSelfManagedIoStop, wudfddi/IPnpCallbackSelfManagedIo::OnSelfManagedIoStop, UMDFDeviceObjectRef_d9eba21f-f9a7-48d2-a8e7-f71a735246bc.xml, IPnpCallbackSelfManagedIo interface, OnSelfManagedIoStop method, IPnpCallbackSelfManagedIo::OnSelfManagedIoStop, umdf.ipnpcallbackselfmanagedio_onselfmanagediostop, wdf.ipnpcallbackselfmanagedio_onselfmanagediostop
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : wudfddi.h
req.include-header : Wudfddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---


# OnSelfManagedIoStop method
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>OnSelfManagedIoStop</b> method is not used in the current version of the UMDF.

## Syntax

````
HRESULT OnSelfManagedIoStop(
  [in] IWDFDevice *pWdfDevice
);
````

## Parameters

`pWdfDevice`




## Return Value

This method is not currently used.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h (include Wudfddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |