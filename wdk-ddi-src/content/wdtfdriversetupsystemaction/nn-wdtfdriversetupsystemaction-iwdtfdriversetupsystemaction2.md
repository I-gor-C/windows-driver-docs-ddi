---
UID: NN:wdtfdriversetupsystemaction.IWDTFDriverSetupSystemAction2
title: IWDTFDriverSetupSystemAction2
author: windows-driver-content
description: Defines operations that control the system during driver setup.
old-location: dtf\iwdtfdriversetupsystemaction2.htm
old-project: dtf
ms.assetid: d825c8de-7565-494a-ae49-be404493945e
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFDriverSetupSystemAction2, IWDTFDriverSetupSystemAction2 interface [Windows Device Testing Framework], IWDTFDriverSetupSystemAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFDriverSetupSystemAction2, dtf.iwdtfdriversetupsystemaction2, wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfdriversetupsystemaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverSetupSystemAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverSetupSystemAction.Interop.dll
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
-	WDTFDriverSetupSystemAction.Interop.dll
api_name:
-	IWDTFDriverSetupSystemAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFDriverSetupSystemAction2 interface

Defines operations that control the system during driver setup.

## Methods

<p>The <b>IWDTFDriverSetupSystemAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFDriverSetupSystemAction2::ClearTriageLogs](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-cleartriagelogs.md) | Clears the system device setup triage logs. |
| [IWDTFDriverSetupSystemAction2::ImportDriverPackage](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-importdriverpackage.md) | Imports a driver packge to the system driver store. |
| [IWDTFDriverSetupSystemAction2::IsImported](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-isimported.md) | Returns a value that indicates whether a package has already been imported. |
| [IWDTFDriverSetupSystemAction2::RemoveDriverPackage](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-removedriverpackage.md) | Removes a driver package from the driver store. |
| [IWDTFDriverSetupSystemAction2::RescanAllDevices](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-rescanalldevices.md) | Re-enumerates all devices in the system. |
| [IWDTFDriverSetupSystemAction2::SnapTriageLogs](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-snaptriagelogs.md) | Copies the driver setup triage logs. |
| [IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents](nf-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2-waitnopendinginstallevents.md) | Waits until all device installations have completed. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfdriversetupsystemaction.h |