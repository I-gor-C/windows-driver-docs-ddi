---
UID: NS.DXGIDDI.DXGI1_3_DDI_BASE_FUNCTIONS
title: DXGI1_3_DDI_BASE_FUNCTIONS
author: windows-driver-content
description: Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition.
old-location: display\dxgi1_3_ddi_base_functions.htm
old-project: display
ms.assetid: F857BA54-A572-4376-83F3-573F90033261
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DXGI1_3_DDI_BASE_FUNCTIONS, DXGI1_3_DDI_BASE_FUNCTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI1_3_DDI_BASE_FUNCTIONS
req.alt-loc: Dxgiddi.h
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
---

# DXGI1_3_DDI_BASE_FUNCTIONS structure



## -description
Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition.


## -syntax

````
typedef struct DXGI1_3_DDI_BASE_FUNCTIONS {
  HRESULT (__stdcall *pfnPresent)(DXGI_DDI_ARG_PRESENT*);
  HRESULT (__stdcall *pfnGetGammaCaps)(DXGI_DDI_ARG_GET_GAMMA_CONTROL_CAPS*);
  HRESULT (__stdcall *pfnSetDisplayMode)(DXGI_DDI_ARG_SETDISPLAYMODE*);
  HRESULT (__stdcall *pfnSetResourcePriority)(DXGI_DDI_ARG_SETRESOURCEPRIORITY*);
  HRESULT (__stdcall *pfnQueryResourceResidency)(DXGI_DDI_ARG_QUERYRESOURCERESIDENCY*);
  HRESULT (__stdcall *pfnRotateResourceIdentities)(DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES*);
  HRESULT (__stdcall *pfnBlt)(DXGI_DDI_ARG_BLT*);
  HRESULT (__stdcall *pfnResolveSharedResource)(DXGI_DDI_ARG_RESOLVESHAREDRESOURCE*);
  HRESULT (__stdcall *pfnBlt1)(DXGI_DDI_ARG_BLT1*);
  HRESULT (__stdcall *pfnOfferResources)(DXGI_DDI_ARG_OFFERRESOURCES*);
  HRESULT (__stdcall *pfnReclaimResources)(DXGI_DDI_ARG_RECLAIMRESOURCES*);
  HRESULT (__stdcall *pfnGetMultiPlaneOverlayCaps)(DXGI_DDI_ARG_GETMULTIPLANEOVERLAYCAPS*);
  HRESULT (__stdcall *pfnGetMultiplaneOverlayGroupCaps)(DXGI_DDI_ARG_GETMULTIPLANEOVERLAYGROUPCAPS *pfnGetMultiplaneOverlayGroupCaps);
  HRESULT (__stdcall *pfnReserved1)( void*);
  HRESULT (__stdcall *pfnPresentMultiPlaneOverlay)(DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY *pfnPresentMultiPlaneOverlay);
  HRESULT (__stdcall *pfnReserved2)(void*);
  HRESULT (__stdcall *pfnPresent1)(DXGI_DDI_ARG_PRESENT1*);
  HRESULT (__stdcall *pfnCheckPresentDurationSupport)(DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT*);
} DXGI1_3_DDI_BASE_FUNCTIONS;
````


## -struct-fields

### -field pfnPresent

A pointer to the driver's <a href="display.presentdxgi">PresentDXGI</a> function.

### -field pfnGetGammaCaps

A pointer to the driver's <a href="display.getgammacapsdxgi">GetGammaCapsDXGI</a> function.

### -field pfnSetDisplayMode

A pointer to the driver's <a href="display.setdisplaymodedxgi">SetDisplayModeDXGI</a> function.

### -field pfnSetResourcePriority

A pointer to the driver's <a href="display.setresourceprioritydxgi">SetResourcePriorityDXGI</a> function.

### -field pfnQueryResourceResidency

A pointer to the driver's <a href="display.queryresourceresidencydxgi">QueryResourceResidencyDXGI</a> function.

### -field pfnRotateResourceIdentities

A pointer to the driver's <a href="display.rotateresourceidentitiesdxgi">RotateResourceIdentitiesDXGI</a> function.

### -field pfnBlt

A pointer to the driver's <a href="display.bltdxgi">BltDXGI</a> function.

### -field pfnResolveSharedResource

A pointer to the driver's <a href="display.resolvesharedresourcedxgi">ResolveSharedResourceDXGI</a> function.

### -field pfnBlt1

A pointer to the driver's  <a href="display.blt1dxgi">Blt1DXGI</a> function.

### -field pfnOfferResources

A pointer to the driver's <a href="display.pfnofferresources">pfnOfferResources</a> function.

### -field pfnReclaimResources

A pointer to the driver's <a href="display.pfnreclaimresources">pfnReclaimResources</a> function.

### -field pfnGetMultiPlaneOverlayCaps

A pointer to the driver's <a href="display.pfngetmultiplaneoverlaycaps">pfnGetMultiPlaneOverlayCaps</a> function.

### -field pfnGetMultiplaneOverlayGroupCaps

A pointer to the driver's <a href="display.pfngetmultiplaneoverlaygroupcaps">pfnGetMultiplaneOverlayGroupCaps</a> function.

### -field pfnReserved1

Reserved for system use.

### -field pfnPresentMultiPlaneOverlay

A pointer to the driver's <a href="..\dxgiddi\nc-dxgiddi-pfnddxgiddi_present_multiplane_overlaycb.md">pfnPresentMultiplaneOverlay (DXGI)</a> function.

### -field pfnReserved2

Reserved for system use.

### -field pfnPresent1

A pointer to the driver's <a href="display.pfnpresent1_dxgi_">pfnPresent1(DXGI)</a> function.

### -field pfnCheckPresentDurationSupport

A pointer to the driver's <a href="display.pfncheckpresentdurationsupport_dxgi_">pfnCheckPresentDurationSupport(DXGI)</a> function.

## -remarks
For more info on how to use this structure, see <a href="https://msdn.microsoft.com/3a49d7cb-984f-4e4f-a549-5c0442e1c45a">Supporting the DXGI DDI</a>.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
WDDM 1.3 and later
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi_ddi_base_args.md">DXGI_DDI_BASE_ARGS</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi_ddi_base_functions.md">DXGI_DDI_BASE_FUNCTIONS</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi1_2_ddi_base_functions.md">DXGI1_2_DDI_BASE_FUNCTIONS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI1_3_DDI_BASE_FUNCTIONS structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>