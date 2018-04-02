---
UID: NN:wdtfdriverpackageaction.IWDTFDriverPackageAction2
title: IWDTFDriverPackageAction2
author: windows-driver-content
description: Defines operations and properties that represent a driver package for imported and pre-imported driver packages.
old-location: dtf\iwdtfdriverpackageaction2.htm
old-project: dtf
ms.assetid: aa66280d-c32e-4d1c-bcc8-aa2719b61010
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFDriverPackageAction2, IWDTFDriverPackageAction2 interface [Windows Device Testing Framework], IWDTFDriverPackageAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFDriverPackageAction2, dtf.iwdtfdriverpackageaction2, wdtfdriverpackageaction/IWDTFDriverPackageAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfdriverpackageaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverPackageAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverPackageAction.Interop.dll
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
-	WDTFDriverPackageAction.Interop.dll
api_name:
-	IWDTFDriverPackageAction2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFDriverPackageAction2 interface

Defines operations and properties that represent a driver package for imported and pre-imported
driver packages.

## Methods

<p>The <b>IWDTFDriverPackageAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFDriverPackageAction2::Compare](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-compare.md) | Compares two driver packages. |
| [IWDTFDriverPackageAction2::get_CatalogFile](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_catalogfile.md) | Gets the catalog file name. |
| [IWDTFDriverPackageAction2::get_ClassGuid](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_classguid.md) | Gets the class GUID. |
| [IWDTFDriverPackageAction2::get_ClassName](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_classname.md) | Gets the class name. |
| [IWDTFDriverPackageAction2::get_Date](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_date.md) | Gets the driver package date. |
| [IWDTFDriverPackageAction2::get_DigitalSigner](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_digitalsigner.md) | Gets the digital signer. |
| [IWDTFDriverPackageAction2::get_HasCatalog](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_hascatalog.md) | Gets a value that indicates whether the driver package has a catalog. |
| [IWDTFDriverPackageAction2::get_InfFileName](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_inffilename.md) | Gets the INF file name. |
| [IWDTFDriverPackageAction2::get_IsDigitalSigned](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_isdigitalsigned.md) | Gets a value that indicates whether the driver package is signed. |
| [IWDTFDriverPackageAction2::get_IsImported](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_isimported.md) | Gets a value that indicates whether the driver package is imported. |
| [IWDTFDriverPackageAction2::get_Provider](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_provider.md) | Gets the driver package provider. |
| [IWDTFDriverPackageAction2::get_Version](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-get_version.md) | Gets the driver package version. |
| [IWDTFDriverPackageAction2::GetQueryForDeviceThatCanUsePackage](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-getqueryfordevicethatcanusepackage.md) | Returns an SDEL statement that queries for all devices that can use the driver package. |
| [IWDTFDriverPackageAction2::GetQueryForDeviceUsingPackage](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-getqueryfordeviceusingpackage.md) | Returns an SDEL statement that queries for all devices that use the driver package. |
| [IWDTFDriverPackageAction2::SetPackageInfFileName](nf-wdtfdriverpackageaction-iwdtfdriverpackageaction2-setpackageinffilename.md) | Sets the pre-imported driver package path. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfdriverpackageaction.h |