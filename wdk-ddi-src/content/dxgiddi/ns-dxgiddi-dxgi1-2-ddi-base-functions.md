---
UID: NS.dxgiddi.DXGI1_2_DDI_BASE_FUNCTIONS
title: DXGI1_2_DDI_BASE_FUNCTIONS
author: windows-driver-content
description: Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.2 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition.
old-location: display\dxgi1_2_ddi_base_functions.htm
old-project: display
ms.assetid: 7A1CD16A-4B7A-40FE-8650-AAD8CAC10FB0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI1_2_DDI_BASE_FUNCTIONS, DXGI1_2_DDI_BASE_FUNCTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8,WDDM 1.2 and later
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI1_2_DDI_BASE_FUNCTIONS
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
req.iface: 
---

# DXGI1_2_DDI_BASE_FUNCTIONS structure



## -description
<p>Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.2 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition.</p>


## -syntax

````
typedef struct _DXGI1_2_DDI_BASE_FUNCTIONS {
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
  HRESULT (__stdcall *pfnGetMultiPlaneOverlayFilterRange)(void*);
  HRESULT (__stdcall *pfnCheckMultiPlaneOverlaySupport)(DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT*);
  HRESULT (__stdcall *pfnPresentMultiPlaneOverlay)(DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY*);
} DXGI1_2_DDI_BASE_FUNCTIONS;
````


## -struct-fields
<dl>

### -field <b>pfnPresent</b>

<dd>
<p>A pointer to the driver's <a href="display.presentdxgi">PresentDXGI</a> function.</p>
</dd>

### -field <b>pfnGetGammaCaps</b>

<dd>
<p>A pointer to the driver's <a href="display.getgammacapsdxgi">GetGammaCapsDXGI</a> function.</p>
</dd>

### -field <b>pfnSetDisplayMode</b>

<dd>
<p>A pointer to the driver's <a href="display.setdisplaymodedxgi">SetDisplayModeDXGI</a> function.</p>
</dd>

### -field <b>pfnSetResourcePriority</b>

<dd>
<p>A pointer to the driver's <a href="display.setresourceprioritydxgi">SetResourcePriorityDXGI</a> function.</p>
</dd>

### -field <b>pfnQueryResourceResidency</b>

<dd>
<p>A pointer to the driver's <a href="display.queryresourceresidencydxgi">QueryResourceResidencyDXGI</a> function.</p>
</dd>

### -field <b>pfnRotateResourceIdentities</b>

<dd>
<p>A pointer to the driver's <a href="display.rotateresourceidentitiesdxgi">RotateResourceIdentitiesDXGI</a> function.</p>
</dd>

### -field <b>pfnBlt</b>

<dd>
<p>A pointer to the driver's <a href="display.bltdxgi">BltDXGI</a> function.</p>
</dd>

### -field <b>pfnResolveSharedResource</b>

<dd>
<p>A pointer to the driver's <a href="display.resolvesharedresourcedxgi">ResolveSharedResourceDXGI</a> function.</p>
</dd>

### -field <b>pfnBlt1</b>

<dd>
<p>A pointer to the driver's  <a href="display.blt1dxgi">Blt1DXGI</a> function.</p>
</dd>

### -field <b>pfnOfferResources</b>

<dd>
<p>A pointer to the driver's <a href="display.pfnofferresources">pfnOfferResources</a> function.</p>
</dd>

### -field <b>pfnReclaimResources</b>

<dd>
<p>A pointer to the driver's <a href="display.pfnreclaimresources">pfnReclaimResources</a> function.</p>
</dd>

### -field <b>pfnGetMultiPlaneOverlayCaps</b>

<dd>
<p>A pointer to the driver's <a href="display.pfngetmultiplaneoverlaycaps">pfnGetMultiPlaneOverlayCaps</a> function. Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnGetMultiPlaneOverlayFilterRange</b>

<dd>
<p>This member is reserved and should be set to zero. Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnCheckMultiPlaneOverlaySupport</b>

<dd>
<p>A pointer to the driver's <a href="display.pfncheckmultiplaneoverlaysupport__dxgi_">pfnCheckMultiPlaneOverlaySupport (DXGI)</a> function. Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pfnPresentMultiPlaneOverlay</b>

<dd>
<p>A pointer to the driver's <a href="display.pfnpresentmultiplaneoverlay__dxgi_">pfnPresentMultiplaneOverlay (DXGI)</a> function. Supported starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.2 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-base-args.md">DXGI_DDI_BASE_ARGS</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-base-functions.md">DXGI_DDI_BASE_FUNCTIONS</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi1-3-ddi-base-functions.md">DXGI1_3_DDI_BASE_FUNCTIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI1_2_DDI_BASE_FUNCTIONS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
