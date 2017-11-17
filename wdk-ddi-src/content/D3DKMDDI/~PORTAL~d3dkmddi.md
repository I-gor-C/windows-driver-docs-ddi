# Declarations in the d3dkmddi header
This header D3Dkmddi contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DXGK_GDIARG_STRETCHBLT structure](ns-d3dkmddi--dxgk-gdiarg-stretchblt.md) | The DXGK_GDIARG_STRETCHBLT structure describes the characteristics of a GDI hardware-accelerated stretch bit-block transfer (bitblt) operation. |
| [DXGK_PATCHFLAGS structure](ns-d3dkmddi--dxgk-patchflags.md) | The DXGK_PATCHFLAGS structure identifies, in bit-field flags, information about the direct memory access (DMA) buffer that requires patching. |
| [DXGK_SET_TIMING_RESULTS structure](ns-d3dkmddi--dxgk-set-timing-results.md) | Structure to report result flags from the SetTiming call which apply to the complete call rather than individual paths. |
| [DXGKARG_PRESENT_DISPLAYONLY structure](ns-d3dkmddi--dxgkarg-present-displayonly.md) | Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation. |
| [DXGK_PAGE_TABLE_LEVEL_DESC structure](ns-d3dkmddi--dxgk-page-table-level-desc.md) | The DXGK_PAGE_TABLE_LEVEL_DESC structure describes capabilities that are applied at the page level. |
| [DXGK_CONTEXTINFO_CAPS structure](ns-d3dkmddi--dxgk-contextinfo-caps.md) | DXGK_CONTEXTINFO_CAPS is used to describe the capabilities supported by a driver. |
| [DXGKARG_PREEMPTCOMMAND structure](ns-d3dkmddi--dxgkarg-preemptcommand.md) | The DXGKARG_PREEMPTCOMMAND structure describes a command that a display miniport driver must use to preempt a direct memory access (DMA) buffer that the DxgkDdiSubmitCommand function previously submitted to the hardware command execution unit. |
| [DXGK_GDIARG_COLORFILL structure](ns-d3dkmddi--dxgk-gdiarg-colorfill.md) | The DXGK_GDIARG_COLORFILL structure describes the characteristics of a GDI hardware-accelerated color fill operation. |
| [DXGK_QUERYDISPLAYIDOUT structure](ns-d3dkmddi--dxgk-querydisplayidout.md) | Used to query a display ID. |
| [DXGK_GDIARG_BITBLT structure](ns-d3dkmddi--dxgk-gdiarg-bitblt.md) | The DXGK_GDIARG_BITBLT structure describes the characteristics of a GDI hardware-accelerated bit-block transfer (bitblt) with no stretching. |
| [DXGK_RENDERKM_COMMAND structure](ns-d3dkmddi--dxgk-renderkm-command.md) | The DXGK_RENDERKM_COMMAND structure is used to construct a command buffer to control GDI hardware-accelerated rendering. |
| [DXGKARG_SWITCHTOHWCONTEXTLIST structure](ns-d3dkmddi--dxgkarg-switchtohwcontextlist.md) | TBD |
| [DXGK_ALLOCATIONUSAGEINFO1 structure](ns-d3dkmddi--dxgk-allocationusageinfo1.md) | The DXGK_ALLOCATIONUSAGEINFO1 structure describes how an allocation can be used in DMA buffering. |
| [DXGKARGCB_CREATECONTEXTALLOCATION structure](ns-d3dkmddi--dxgkargcb-createcontextallocation.md) | Specifies the allocation attributes of a GPU context or device-specific context. |
| [DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure](ns-d3dkmddi--dxgk-setvidpnsourceaddress-flags.md) | The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's DxgkDdiSetVidPnSourceAddress or DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay functions. |
| [DXGK_DEVICEINFOFLAGS structure](ns-d3dkmddi--dxgk-deviceinfoflags.md) | The DXGK_DEVICEINFOFLAGS structure identifies, in bit-field flags, information about a graphics device. |
| [DXGK_BUILDPAGINGBUFFER_COPY_RANGE structure](ns-d3dkmddi--dxgk-buildpagingbuffer-copy-range.md) | DXGK_BUILDPAGINGBUFFER_COPY_RANGE is used as part of a page table entry copy operation. |
| [DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 structure](ns-d3dkmddi--dxgkarg-checkmultiplaneoverlaysupport2.md) | DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 is passed to the DxgkDdiCheckMultiPlaneOverlaySupport2 function to determine whether a specific multi-plane overlay configuration is supported. |
| [DXGKARG_OPENALLOCATION structure](ns-d3dkmddi--dxgkarg-openallocation.md) | The DXGKARG_OPENALLOCATION structure describes allocations that the display miniport driver should open. |
| [DXGK_MONITORSOURCEMODESET_INTERFACE structure](ns-d3dkmddi--dxgk-monitorsourcemodeset-interface.md) | The DXGK_MONITORSOURCEMODESET_INTERFACE structure contains pointers to functions that belong to the Monitor Source Mode Set interface, which is implemented by the video present network (VidPN) manager. |
| [DXGK_QUERYGPUMMUCAPSIN structure](ns-d3dkmddi--dxgk-querygpummucapsin.md) | The DXGK_QUERYGPUMMUCAPSIN structure holds the index of the adapter being queried. |
| [D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS structure](ns-d3dkmddi--d3dkmt-present-display-only-flags.md) | Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation. |
| [DXGK_SEGMENTDESCRIPTOR2 structure](ns-d3dkmddi--dxgk-segmentdescriptor2.md) | The DXGK_SEGMENTDESCRIPTOR2 structure is reserved for system use. Do not use it in your driver. |
| [DXGK_VIDSCHCAPS structure](ns-d3dkmddi--dxgk-vidschcaps.md) | The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support. |
| [DXGK_PRESENTMULTIPLANEOVERLAYINFO structure](ns-d3dkmddi--dxgk-presentmultiplaneoverlayinfo.md) | Specifies info on a VidPN input and an overlay plane to display. |
| [DXGK_BUILDPAGINGBUFFER_FLUSHTLB structure](ns-d3dkmddi--dxgk-buildpagingbuffer-flushtlb.md) | DXGK_BUILDPAGINGBUFFER_FLUSHTLB is used as part of a flush translation look-aside buffer (TLB) operation. |
| [DXGKARG_UPDATEOVERLAY structure](ns-d3dkmddi--dxgkarg-updateoverlay.md) | The DXGKARG_UPDATEOVERLAY structure describes parameters for modifying an overlay. |
| [DXGK_VIDPN_INTERFACE structure](ns-d3dkmddi--dxgk-vidpn-interface.md) | TBD |
| [DXGK_GPUENGINETOPOLOGY structure](ns-d3dkmddi--dxgk-gpuenginetopology.md) | The DXGK_GPUENGINETOPOLOGY structure describes the graphics processing unit (GPU)-engine topology that a driver can support. |
| [DXGK_FLIPCAPS structure](ns-d3dkmddi--dxgk-flipcaps.md) | The DXGK_FLIPCAPS structure identifies flipping capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGKARG_DESTROYALLOCATION structure](ns-d3dkmddi--dxgkarg-destroyallocation.md) | The DXGKARG_DESTROYALLOCATION structure describes how the display miniport driver should release allocations. |
| [DXGKARG_RESETHWENGINE structure](ns-d3dkmddi--dxgkarg-resethwengine.md) | TBD |
| [DXGKARG_HISTORYBUFFERPRECISION structure](ns-d3dkmddi--dxgkarg-historybufferprecision.md) | Indicates info about the precision of history buffer data used by the display miniport driver. |
| [DXGK_SET_TIMING_PATH_INFO structure](ns-d3dkmddi--dxgk-set-timing-path-info.md) | Structure to hold information to modify SetTiming path. |
| [DXGKARG_PATCH structure](ns-d3dkmddi--dxgkarg-patch.md) | The DXGKARG_PATCH structure describes a direct memory access (DMA) buffer that requires patching (that is, requires the assignment of physical addresses). |
| [DXGKARG_POSTMULTIPLANEOVERLAYPRESENT structure](ns-d3dkmddi--dxgkarg-postmultiplaneoverlaypresent.md) | Contains arguments for the DxgkDdiPostMultiPlaneOverlayPresent function. |
| [DXGK_UPDATEHWCONTEXTSTATE_FLAGS structure](ns-d3dkmddi--dxgk-updatehwcontextstate-flags.md) | Used to update the HW context state flags. |
| [DXGK_OPENALLOCATIONINFO structure](ns-d3dkmddi--dxgk-openallocationinfo.md) | The DXGK_OPENALLOCATIONINFO structure contains handles to nondevice-specific and device-specific allocations that the DxgkDdiOpenAllocation function associates. |
| [DXGKARG_RECOMMENDMONITORMODES structure](ns-d3dkmddi--dxgkarg-recommendmonitormodes.md) | The DXGKARG_RECOMMENDMONITORMODES structure contains arguments for the DxgkDdiRecommendMonitorModes function. |
| [DXGK_MODE_BEHAVIOR_FLAGS structure](ns-d3dkmddi--dxgk-mode-behavior-flags.md) | TBD |
| [DXGKARG_PRESENT structure](ns-d3dkmddi--dxgkarg-present.md) | The DXGKARG_PRESENT structure describes a source-to-primary copy operation. |
| [DXGKARGCB_NOTIFY_INTERRUPT_DATA structure](ns-d3dkmddi--dxgkargcb-notify-interrupt-data.md) | The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information. |
| [DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES3 structure](ns-d3dkmddi--dxgk-multiplane-overlay-attributes3.md) | A structure containing the attributes used for the image in a multiplane overlay. |
| [DXGKARG_RESETENGINE structure](ns-d3dkmddi--dxgkarg-resetengine.md) | Specifies a node within the physical display adapter that can be reset when the display port driver's GPU scheduler calls the DxgkDdiResetEngine function to request a reset operation. |
| [DXGK_ENGINESTATUS structure](ns-d3dkmddi--dxgk-enginestatus.md) | Indicates the progress of a node within an active physical display adapter (engine) specified by a DXGKARG_QUERYENGINESTATUS structure. |
| [DXGK_ALLOCATIONLIST structure](ns-d3dkmddi--dxgk-allocationlist.md) | The DXGK_ALLOCATIONLIST structure describes an allocation specification that is used in direct memory access (DMA) buffering. |
| [DXGKARG_SETDISPLAYPRIVATEDRIVERFORMAT structure](ns-d3dkmddi--dxgkarg-setdisplayprivatedriverformat.md) | The DXGKARG_SETDISPLAYPRIVATEDRIVERFORMAT structure describes how to set the private-format attribute for a video present source. |
| [DXGK_SEGMENTDESCRIPTOR3 structure](ns-d3dkmddi--dxgk-segmentdescriptor3.md) | Contains information about a driver-supported segment that is composed of both BIOS-reserved memory (which is purged during a transition to a low-power state) and driver-reserved memory. |
| [DXGK_INTERFACESPECIFICDATA structure](ns-d3dkmddi--dxgk-interfacespecificdata.md) | The DXGK_INTERFACESPECIFICDATA structure is reserved for system use. Do not use it in your driver. |
| [DXGK_PREEMPTCOMMANDFLAGS structure](ns-d3dkmddi--dxgk-preemptcommandflags.md) | The DXGK_PREEMPTCOMMANDFLAGS structure specifies a union that contains either a structure with a reserved member or a 32-bit value. No bit-field flags are currently defined. |
| [DXGK_SET_TIMING_FLAGS structure](ns-d3dkmddi--dxgk-set-timing-flags.md) | Structure to hold flags used to modify SetTiming behavior. Currently no flags are defined. |
| [DXGKARG_SETTARGETGAMMA structure](ns-d3dkmddi--dxgkarg-settargetgamma.md) | Used to hold the arguments for DXGKDDI_SETTARGETGAMMA. |
| [DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES structure](ns-d3dkmddi--dxgk-multiplane-overlay-attributes.md) | Used by the display miniport driver to specify overlay plane attributes. |
| [DXGKARG_DESCRIBEALLOCATION structure](ns-d3dkmddi--dxgkarg-describeallocation.md) | The DXGKARG_DESCRIBEALLOCATION structure describes an existing allocation. |
| [DXGK_CREATECONTEXTALLOCATIONFLAGS structure](ns-d3dkmddi--dxgk-createcontextallocationflags.md) | TBD |
| [DXGK_HDR_METADATA structure](ns-d3dkmddi--dxgk-hdr-metadata.md) | Contains information about the HDR metadata. |
| [DXGK_CREATEPROCESSFLAGS structure](ns-d3dkmddi--dxgk-createprocessflags.md) | DXGK_CREATEPROCESSFLAGS is used with DXGKARG_CREATEPROCESS and DxgkDdiCreateProcess to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object. |
| [DXGKARG_VALIDATEUPDATEALLOCPROPERTY structure](ns-d3dkmddi--dxgkarg-validateupdateallocproperty.md) | The DXGARG_VALIDATEUPDATEALLOCPROPERTY structure holds the information needed to validate the parameters to update the properties of an allocation. |
| [DXGKARG_COLLECTDBGINFO_EXT structure](ns-d3dkmddi--dxgkarg-collectdbginfo-ext.md) | The DXGKARG_COLLECTDBGINFO_EXT structure describes extension information for a debug report. |
| [DXGKARG_UPDATEHWCONTEXTSTATE structure](ns-d3dkmddi--dxgkarg-updatehwcontextstate.md) | Used to update the context state. |
| [DXGK_MONITORDESCRIPTORSET_INTERFACE structure](ns-d3dkmddi--dxgk-monitordescriptorset-interface.md) | The DXGK_MONITORDESCRIPTORSET_INTERFACE structure contains pointers to functions that belong to the Monitor Descriptor Set Interface, which is implemented by the video present network (VidPN) manager. |
| [DXGK_QUERYADAPTERINFOFLAGS structure](ns-d3dkmddi--dxgk-queryadapterinfoflags.md) | TBD |
| [DXGK_PRIMARYDATA structure](ns-d3dkmddi--dxgk-primarydata.md) | TBD |
| [DXGK_PRESENTATIONCAPS structure](ns-d3dkmddi--dxgk-presentationcaps.md) | The DXGK_PRESENTATIONCAPS structure identifies presentation capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGKARG_SETPOINTERSHAPE structure](ns-d3dkmddi--dxgkarg-setpointershape.md) | The DXGKARG_SETPOINTERSHAPE structure describes the appearance of the mouse pointer and the location that it should be displayed in. |
| [DXGKARGCB_INVALIDATEHWCONTEXT structure](ns-d3dkmddi--dxgkargcb-invalidatehwcontext.md) | TBD |
| [DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL structure](ns-d3dkmddi--dxgk-buildpagingbuffer-transfervirtual.md) | DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL is used as part of an allocation transfer operation. |
| [DXGK_SETPOINTERPOSITIONFLAGS structure](ns-d3dkmddi--dxgk-setpointerpositionflags.md) | The DXGK_SETPOINTERPOSITIONFLAGS structure identifies, in bit-field flags, information about a mouse pointer. |
| [DXGK_VIDMMCAPS structure](ns-d3dkmddi--dxgk-vidmmcaps.md) | The DXGK_VIDMMCAPS structure identifies the video memory management capabilities that a display miniport driver can support. |
| [DXGKARG_SUBMITCOMMANDVIRTUAL structure](ns-d3dkmddi--dxgkarg-submitcommandvirtual.md) | DXGKARG_SUBMITCOMMANDVIRTUAL is used to submit a direct memory access (DMA) buffer to a context that supports virtual addressing with the DxgkDdiSubmitCommandVirtualdevice driver interface (DDI). |
| [DXGKARG_CLOSEALLOCATION structure](ns-d3dkmddi--dxgkarg-closeallocation.md) | The DXGKARG_CLOSEALLOCATION structure describes allocations that the display miniport driver should close. |
| [DXGK_QUERYSEGMENTOUT2 structure](ns-d3dkmddi--dxgk-querysegmentout2.md) | The DXGK_QUERYSEGMENTOUT2 structure is reserved for system use. Do not use it in your driver. |
| [DXGK_QAITARGETIN structure](ns-d3dkmddi--dxgk-qaitargetin.md) | Used to integrate a target. |
| [DXGKCB_NOTIFY_MPO_VSYNC_FLAGS structure](ns-d3dkmddi--dxgkcb-notify-mpo-vsync-flags.md) | A structure containing the flags set by the driver to process a flip entry. |
| [DXGKARG_SUBMITCOMMAND structure](ns-d3dkmddi--dxgkarg-submitcommand.md) | The DXGKARG_SUBMITCOMMAND structure describes the direct memory access (DMA) buffer that a display miniport driver submits to the hardware command execution unit. |
| [DXGK_GDIARG_CLEARTYPEBLEND structure](ns-d3dkmddi--dxgk-gdiarg-cleartypeblend.md) | The DXGK_GDIARG_CLEARTYPEBLEND structure describes the characteristics of a GDI hardware-accelerated ClearType and antialiased text pixel blending operation. |
| [DXGKARG_CREATEPERIODICFRAMENOTIFICATION structure](ns-d3dkmddi--dxgkarg-createperiodicframenotification.md) | The arguments needed to create a periodic frame notification. |
| [DXGKARG_ISSUPPORTEDVIDPN structure](ns-d3dkmddi--dxgkarg-issupportedvidpn.md) | The DXGKARG_ISSUPPORTEDVIDPN structure contains arguments for the DxgkDdiIsSupportedVidPn function. The DxgkDdiIsSupportedVidPn function determines whether a specified video present network (VidPN) is supported on a display adapter. |
| [DXGK_SUBMITCOMMANDFLAGS structure](ns-d3dkmddi--dxgk-submitcommandflags.md) | The DXGK_SUBMITCOMMANDFLAGS structure identifies, in bit-field flags, information about a direct memory access (DMA) buffer to submit to the graphics processing unit (GPU). |
| [DXGK_DESTROYALLOCATIONFLAGS structure](ns-d3dkmddi--dxgk-destroyallocationflags.md) | The DXGK_DESTROYALLOCATIONFLAGS structure identifies how to release allocations. |
| [DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO2 structure](ns-d3dkmddi--dxgk-multiplane-overlay-vsync-info2.md) | Used by new drivers to report per-plane flip completion after a VSYNC. |
| [DXGKARG_QUERYVIDPNHWCAPABILITY structure](ns-d3dkmddi--dxgkarg-queryvidpnhwcapability.md) | TBD |
| [DXGK_PHYSICALADAPTERCAPS structure](ns-d3dkmddi--dxgk-physicaladaptercaps.md) | The DXGK_PHYSICALADAPTERCAPS structure is used to report details of a physical adapter. |
| [DXGKARG_SETTARGETCONTENTTYPE structure](ns-d3dkmddi--dxgkarg-settargetcontenttype.md) | Used to hold the arguments for DXGKDDI_SETTARGETCONTENTTYPE. |
| [DXGK_HISTORY_BUFFER structure](ns-d3dkmddi--dxgk-history-buffer.md) | Specifies a history buffer that stores time stamps that record GPU activity throughout the execution lifetime of a direct memory access (DMA) buffer. |
| [DXGK_QUERYSEGMENTIN4 structure](ns-d3dkmddi--dxgk-querysegmentin4.md) | The DXGK_QUERYSEGMENTIN4 structure is used to specify the adapter to query. |
| [DXGKARG_SETVIDPNSOURCEVISIBILITY structure](ns-d3dkmddi--dxgkarg-setvidpnsourcevisibility.md) | The DXGKARG_SETVIDPNSOURCEVISIBILITY structure contains arguments for the DxgkDdiSetVidPnSourceVisibility function. |
| [DXGKARGCB_MAPCONTEXTALLOCATION structure](ns-d3dkmddi--dxgkargcb-mapcontextallocation.md) | DXGKARGCB_MAPCONTEXTALLOCATION is used with DxgkCbMapContextAllocation to map a graphics processing unit (GPU) virtual address to the specified context allocation. |
| [DXGK_MULTIPLANE_OVERLAY_PLANE structure](ns-d3dkmddi--dxgk-multiplane-overlay-plane.md) | Specifies an overlay plane to display in a call to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function. |
| [DXGK_POWER_P_STATE structure](ns-d3dkmddi--dxgk-power-p-state.md) | Reserved for system use. Do not use it in your driver. |
| [DXGK_ALLOCATIONINFOFLAGS_WDDM2_0 structure](ns-d3dkmddi--dxgk-allocationinfoflags-wddm2-0.md) | TBD |
| [DXGK_SEGMENTDESCRIPTOR4 structure](ns-d3dkmddi--dxgk-segmentdescriptor4.md) | The DXGK_SEGMENTDESCRIPTOR4 structure describes a programmable CPU host aperture. |
| [DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2 structure](ns-d3dkmddi--dxgk-multiplane-overlay-plane-with-source2.md) | Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for multi-plane overlays. |
| [DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT structure](ns-d3dkmddi--dxgkarg-checkmultiplaneoverlaysupport.md) | Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport function to check details on hardware support for multiplane overlays. |
| [DXGK_GAMMARAMPCAPS structure](ns-d3dkmddi--dxgk-gammarampcaps.md) | The DXGK_GAMMARAMPCAPS structure identifies gamma-ramp capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGKARG_STOPCAPTURE structure](ns-d3dkmddi--dxgkarg-stopcapture.md) | The DXGKARG_STOPCAPTURE structure contains the handle to the allocation that is used for a capture buffer. |
| [DXGK_TRANSFERFLAGS structure](ns-d3dkmddi--dxgk-transferflags.md) | The DXGK_TRANSFERFLAGS structure identifies the type of transfer operation to set up in a call to the DxgkDdiBuildPagingBuffer function. |
| [DXGKARG_COMMITVIDPN structure](ns-d3dkmddi--dxgkarg-commitvidpn.md) | The DXGKARG_COMMITVIDPN structure holds arguments for the DxgkDdiCommitVidPn function. The DxgkDdiCommitVidPn function makes a specified video present network (VidPN) active on a display adapter. |
| [DXGK_QUERYSEGMENTMEMORYSTATE structure](ns-d3dkmddi--dxgk-querysegmentmemorystate.md) | DXGK_QUERYSEGMENTMEMORYSTATE is used with DxgkDdiQueryAdapterInfo to query invalid graphics processing unit (GPU) memory ranges. |
| [DXGK_POWER_RUNTIME_STATE structure](ns-d3dkmddi--dxgk-power-runtime-state.md) | Describes the characteristics of an idle state (an F-state). |
| [DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure](ns-d3dkmddi--dxgkarg-getstandardallocationdriverdata.md) | The DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure describes a standard allocation type. |
| [DXGK_MULTIPLANE_OVERLAY_FLAGS structure](ns-d3dkmddi--dxgk-multiplane-overlay-flags.md) | Identifies a flip operation to be performed on an overlay plane. |
| [DXGKARG_QUERYADAPTERINFO structure](ns-d3dkmddi--dxgkarg-queryadapterinfo.md) | The DXGKARG_QUERYADAPTERINFO structure contains parameters for a query. |
| [DXGKARG_BUILDPAGINGBUFFER structure](ns-d3dkmddi--dxgkarg-buildpagingbuffer.md) | The DXGKARG_BUILDPAGINGBUFFER structure describes parameters for building a paging buffer that is used in a memory-transfer operation. |
| [DXGKARG_RECOMMENDVIDPNTOPOLOGY structure](ns-d3dkmddi--dxgkarg-recommendvidpntopology.md) | The DXGKARG_RECOMMENDVIDPNTOPOLOGY structure contains arguments for the display miniport driver's DxgkDdiRecommendVidPnTopology function. |
| [DXGK_VIDPNTARGETMODESET_INTERFACE structure](ns-d3dkmddi--dxgk-vidpntargetmodeset-interface.md) | The DXGK_VIDPNTARGETMODESET_INTERFACE structure contains pointers to functions that belong to the VidPn Target Mode Set interface, which is implemented by the VidPN manager. |
| [DXGK_ALLOCATIONINFOFLAGS structure](ns-d3dkmddi--dxgk-allocationinfoflags.md) | The DXGK_ALLOCATIONINFOFLAGS structure identifies properties for an allocation. The display miniport driver specifies these flags for the video memory manager. |
| [DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE structure](ns-d3dkmddi--dxgk-buildpagingbuffer-updatepagetable.md) | DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE is used as part of a page table update operation. |
| [DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY structure](ns-d3dkmddi--dxgkarg-setvidpnsourceaddresswithmultiplaneoverlay.md) | Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function. |
| [DXGK_SEGMENTDESCRIPTOR structure](ns-d3dkmddi--dxgk-segmentdescriptor.md) | The DXGK_SEGMENTDESCRIPTOR structure contains information about a segment that the driver supports. |
| [DXGKARG_SETVIDEOPROTECTEDREGION structure](ns-d3dkmddi--dxgkarg-setvideoprotectedregion.md) | TBD |
| [DXGK_QUERYSEGMENTOUT3 structure](ns-d3dkmddi--dxgk-querysegmentout3.md) | Describes memory-segment information that a Windows Display Driver Model (WDDM) 1.2 or later display miniport driver should return from a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGK_DESCRIBEALLOCATIONFLAGS structure](ns-d3dkmddi--dxgk-describeallocationflags.md) | Used in the DXGKARG_DESCRIBEALLOCATION.Flags member to describe whether an existing allocation is being queried for its display mode. |
| [DXGK_POWER_COMPONENT_P_FLAGS structure](ns-d3dkmddi--dxgk-power-component-p-flags.md) | Reserved for system use. Do not use in your driver. |
| [DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES structure](ns-d3dkmddi--dxgk-buildpagingbuffer-copypagetableentries.md) | DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES describes the operation used copy page table entries from one location to another. |
| [DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS structure](ns-d3dkmddi--dxgkargcb-present-displayonly-progress.md) | Provides the progress of a kernel mode display-only driver's (KMDOD) present operation that was requested by the operating system. |
| [DXGK_PHYSICALADAPTERFLAGS structure](ns-d3dkmddi--dxgk-physicaladapterflags.md) | DXGK_PHYSICALADAPTERFLAGS defines a set of flags that used to indicate the type of memory management model that is supported by a device. |
| [DXGK_CREATEALLOCATIONFLAGS structure](ns-d3dkmddi--dxgk-createallocationflags.md) | The DXGK_CREATEALLOCATIONFLAGS structure identifies how to create allocations. |
| [DXGK_QUERYPAGETABLELEVELDESCIN structure](ns-d3dkmddi--dxgk-querypagetableleveldescin.md) | The DXGK_QUERYPAGETABLELEVELDESCIN structure is used to request page level descriptors from the Dxgkrnl Interface. |
| [DXGKARG_UPDATEMONITORLINKINFO structure](ns-d3dkmddi--dxgkarg-updatemonitorlinkinfo.md) | TBD |
| [DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION structure](ns-d3dkmddi--dxgk-multiplane-overlay-post-composition.md) | Specifies information about any additional transforms that should occur after the planes are composed. |
| [DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION structure](ns-d3dkmddi--dxgk-buildpagingbuffer-updatecontextallocation.md) | DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION describes an operation used to update the content of a context or device allocation. |
| [DXGK_QUERYSEGMENTOUT structure](ns-d3dkmddi--dxgk-querysegmentout.md) | The DXGK_QUERYSEGMENTOUT structure describes memory-segment information that the display miniport driver should return from a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE structure](ns-d3dkmddi--dxgk-check-multiplane-overlay-support-plane.md) | Specifies the support attributes that the hardware provides for multiplane overlays. |
| [DXGKARG_RELEASESWIZZLINGRANGE structure](ns-d3dkmddi--dxgkarg-releaseswizzlingrange.md) | The DXGKARG_RELEASESWIZZLINGRANGE structure describes parameters for releasing a swizzling range. |
| [DXGK_PRESENTMULTIPLANEOVERLAYLIST structure](ns-d3dkmddi--dxgk-presentmultiplaneoverlaylist.md) | Specifies an overlay plane to display in a call to the DxgkDdiPresent function. |
| [DXGKARG_RENDERGDI structure](ns-d3dkmddi--dxgkarg-rendergdi.md) | The DXGKARG_RENDERGDI structure is used when submitting Windows Graphics Device Interface (GDI) commands for contexts that support virtual addressing. |
| [DXGK_QUERYSEGMENTOUT4 structure](ns-d3dkmddi--dxgk-querysegmentout4.md) | The DXGK_QUERYSEGMENTOUT4 structure contains memory segment information returned from the driver. |
| [DXGK_QUERYHISTORYBUFFERPRECISIONIN structure](ns-d3dkmddi--dxgk-queryhistorybufferprecisionin.md) | TBD |
| [DXGKARG_QUERYDEPENDENTENGINEGROUP structure](ns-d3dkmddi--dxgkarg-querydependentenginegroup.md) | Describes all nodes on the physical display adapter (engine) that are to be queried when the display port driver's GPU scheduler calls the DxgkDdiQueryDependentEngineGroup function to query node dependencies. |
| [DXGK_INTEGRATEDDISPLAYFLAGS structure](ns-d3dkmddi--dxgk-integrateddisplayflags.md) | Flags which describe simple properties of an integrated display. |
| [DXGKARG_GETSCANLINE structure](ns-d3dkmddi--dxgkarg-getscanline.md) | The DXGKARG_GETSCANLINE structure contains information about a video present target's vertical blanking status. |
| [DXGK_POWER_COMPONENT_FLAGS structure](ns-d3dkmddi--dxgk-power-component-flags.md) | Describes state transition information about a power component. |
| [DXGKARG_CREATEALLOCATION structure](ns-d3dkmddi--dxgkarg-createallocation.md) | The DXGKARG_CREATEALLOCATION structure describes how the display miniport driver should create allocations. |
| [DXGK_POWER_COMPONENT_MAPPING structure](ns-d3dkmddi--dxgk-power-component-mapping.md) | Used in the DXGK_POWER_RUNTIME_COMPONENT.ComponentMapping member to define the standard component types of the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) that describe the power component. |
| [DXGK_POINTERFLAGS structure](ns-d3dkmddi--dxgk-pointerflags.md) | The DXGK_POINTERFLAGS structure identifies mouse pointer capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGK_HISTORY_BUFFER_HEADER structure](ns-d3dkmddi--dxgk-history-buffer-header.md) | Specifies how data is stored in a DXGK_HISTORY_BUFFER history buffer. |
| [DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 structure](ns-d3dkmddi--dxgk-multiplane-overlay-attributes2.md) | DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 is used by the display miniport driver to specify overlay plane attributes. |
| [DXGK_QUERYPHYSICALADAPTERCAPSIN structure](ns-d3dkmddi--dxgk-queryphysicaladaptercapsin.md) | The DXGK_QUERYPHYSICALADAPTERCAPSIN structure is used to query the display driver for the capabilities of the physical display adapter. |
| [DXGKARG_DISPLAYDETECTCONTROL structure](ns-d3dkmddi--dxgkarg-displaydetectcontrol.md) | Used to hold the arguments for DXGKDDI_DISPLAYDETECTCONTROL. |
| [DXGKARG_SETROOTPAGETABLE structure](ns-d3dkmddi--dxgkarg-setrootpagetable.md) | DXGKARG_SETROOTPAGETABLE is used by the DxgkDdiSetRootPageTabledevice driver interface (DDI) to notify a context when its associated root page table is resized or moved in memory. |
| [DXGKARG_RECOMMENDFUNCTIONALVIDPN structure](ns-d3dkmddi--dxgkarg-recommendfunctionalvidpn.md) | The DXGKARG_RECOMMENDFUNCTIONALVIDPN structure contains arguments for the DxgkDdiRecommendFunctionalVidPn function. |
| [DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY structure](ns-d3dkmddi--dxgk-buildpagingbuffer-notifyresidency.md) | DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY describes a residency allocation change operation. |
| [DXGKARG_RENDER structure](ns-d3dkmddi--dxgkarg-render.md) | The DXGKARG_RENDER structure describes members for generating a direct memory access (DMA) buffer from a command buffer. |
| [DXGK_GDIARG_TRANSPARENTBLT structure](ns-d3dkmddi--dxgk-gdiarg-transparentblt.md) | The DXGK_GDIARG_TRANSPARENTBLT structure describes the characteristics of a GDI hardware-accelerated bit-block transfer (bitblt) operation with transparency. |
| [DXGK_QUERYDISPLAYIDIN structure](ns-d3dkmddi--dxgk-querydisplayidin.md) | Used to query a display ID. |
| [DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure](ns-d3dkmddi--dxgk-monitorfrequencyrangeset-interface.md) | The DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure contains pointers to functions that belong to the Monitor Frequency Range Set interface, which is implemented by the video present network (VidPN) manager. |
| [DXGK_QUERYINTEGRATEDDISPLAYOUT structure](ns-d3dkmddi--dxgk-queryintegrateddisplayout.md) | TBD |
| [DXGKARG_SETSTABLEPOWERSTATE structure](ns-d3dkmddi-dxgkarg-setstablepowerstate.md) | TBD |
| [DXGK_DRIVERCAPS structure](ns-d3dkmddi--dxgk-drivercaps.md) | The DXGK_DRIVERCAPS structure describes capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGKARG_COLLECTDBGINFO structure](ns-d3dkmddi--dxgkarg-collectdbginfo.md) | The DXGKARG_COLLECTDBGINFO structure describes information for a debug report. |
| [DXGKARG_CREATEHWQUEUE structure](ns-d3dkmddi--dxgkarg-createhwqueue.md) | TBD |
| [DXGK_SEGMENTFLAGS2 structure](ns-d3dkmddi--dxgk-segmentflags2.md) | The DXGK_SEGMENTFLAGS2 structure is reserved for system use. Do not use it in your driver. |
| [DXGKARG_GETPOSTCOMPOSITIONCAPS structure](ns-d3dkmddi--dxgkarg-getpostcompositioncaps.md) | Arguments for the DxgkDdiGetPostCompositionCaps function. |
| [DXGKARG_GETROOTPAGETABLESIZE structure](ns-d3dkmddi--dxgkarg-getrootpagetablesize.md) | DXGKARG_GETROOTPAGETABLESIZE is used with DxgkDdiGetRootPageTableSize. |
| [DXGKARG_SETTARGETANALOGCOPYPROTECTION structure](ns-d3dkmddi--dxgkarg-settargetanalogcopyprotection.md) | Holds information to set analog copy protection on a display adapter's video present target. |
| [D3DKM_TRANSPARENTBLTFLAGS structure](ns-d3dkmddi--d3dkm-transparentbltflags.md) | The D3DKM_TRANSPARENTBLTFLAGS structure specifies the display adapter's ability to perform a hardware-accelerated bit-block transfer (bitblt) with transparency. |
| [DXGK_DISPLAY_DRIVERCAPS_EXTENSION structure](ns-d3dkmddi--dxgk-display-drivercaps-extension.md) | TBD |
| [DXGK_CREATEDEVICEFLAGS structure](ns-d3dkmddi--dxgk-createdeviceflags.md) | The DXGK_CREATEDEVICEFLAGS structure identifies how to create devices. |
| [DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure](ns-d3dkmddi--dxgk-plane-specific-output-flags.md) | A structure containing the flags that apply to a plane set by the driver. |
| [DXGK_GDIARG_ALPHABLEND structure](ns-d3dkmddi--dxgk-gdiarg-alphablend.md) | The DXGK_GDIARG_ALPHABLEND structure describes the characteristics of a GDI hardware-accelerated alpha blend operation. |
| [DXGK_POWER_P_COMPONENT structure](ns-d3dkmddi--dxgk-power-p-component.md) | Reserved for system use. Do not use it in your driver. |
| [DXGK_DEVICEINFO structure](ns-d3dkmddi--dxgk-deviceinfo.md) | The DXGK_DEVICEINFO structure describes parameters that the Microsoft DirectX graphics kernel subsystem requires from the display miniport driver. |
| [DXGK_COLORIMETRY structure](ns-d3dkmddi--dxgk-colorimetry.md) | Describes colorimetry and closely related fields used to describe overrides from the descriptor retrieved from the display device. |
| [DXGK_PRESENTALLOCATIONINFO structure](ns-d3dkmddi--dxgk-presentallocationinfo.md) | The DXGK_PRESENTALLOCATIONINFO structure is reserved for system use. Do not use it in your driver. |
| [DXGK_UPDATEPAGETABLEFLAGS structure](ns-d3dkmddi--dxgk-updatepagetableflags.md) | DXGK_UPDATEPAGETABLEFLAGS is used as part of a page table update operation. |
| [DXGKARG_ENUMVIDPNCOFUNCMODALITY structure](ns-d3dkmddi--dxgkarg-enumvidpncofuncmodality.md) | The DXGKARG_ENUMVIDPNCOFUNCMODALITY structure contains arguments for the DxgkDdiEnumVidPnCofuncModality function. |
| [DXGKARG_ACQUIRESWIZZLINGRANGE structure](ns-d3dkmddi--dxgkarg-acquireswizzlingrange.md) | The DXGKARG_ACQUIRESWIZZLINGRANGE structure describes parameters for making an allocation accessible through a CPU aperture. |
| [DXGK_ALLOCATIONUSAGEHINT structure](ns-d3dkmddi--dxgk-allocationusagehint.md) | The DXGK_ALLOCATIONUSAGEHINT structure contains allocation usage and version information that is used as a hint about how to use an allocation. |
| [DXGK_ENUM_PIVOT structure](ns-d3dkmddi--dxgk-enum-pivot.md) | The DXGK_ENUM_PIVOT structure identifies either a video present source or a video present target as the enumeration pivot in a call to DxgkDdiEnumVidPnCofuncModality. |
| [DXGK_STANDARD_COLORIMETRY_FLAGS structure](ns-d3dkmddi--dxgk-standard-colorimetry-flags.md) | Flags describing standard colorimetry and related support. |
| [DXGK_SETVIDPNSOURCEADDRESS_OUTPUT_FLAGS structure](ns-d3dkmddi--dxgk-setvidpnsourceaddress-output-flags.md) | A structure containing the flags used to set the VidPN source address. |
| [DXGKARGCB_RELEASEHANDLEDATA structure](ns-d3dkmddi--dxgkargcb-releasehandledata.md) | TBD |
| [DXGKARGCB_GETCAPTUREADDRESS structure](ns-d3dkmddi--dxgkargcb-getcaptureaddress.md) | The DXGKARGCB_GETCAPTUREADDRESS structure describes parameters for retrieving information about a capture buffer that is associated with an allocation. |
| [DXGK_MONITOR_INTERFACE_V2 structure](ns-d3dkmddi--dxgk-monitor-interface-v2.md) | TBD |
| [DXGKARGCB_UPDATECONTEXTALLOCATION structure](ns-d3dkmddi--dxgkargcb-updatecontextallocation.md) | DXGKARGCB_UPDATECONTEXTALLOCATION contains the data used to call DxgkCbUpdateContextAllocation. |
| [DXGKARG_COMMITVIDPN_FLAGS structure](ns-d3dkmddi--dxgkarg-commitvidpn-flags.md) | The DXGKARG_COMMITVIDPN_FLAGS structure identifies details about a call to the DxgkDdiCommitVidPn function. |
| [DXGKARGCB_GETHANDLEDATA structure](ns-d3dkmddi--dxgkargcb-gethandledata.md) | The DXGKARGCB_GETHANDLEDATA structure describes a handle to private data. |
| [DXGKARG_CREATEPROCESS structure](ns-d3dkmddi--dxgkarg-createprocess.md) | DXGKARG_CREATEPROCESS is used with DxgkDdiCreateProcess to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object. |
| [DXGK_BUILDPAGINGBUFFER_SIGNALMONITOREDFENCE structure](ns-d3dkmddi--dxgk-buildpagingbuffer-signalmonitoredfence.md) | TBD |
| [DXGKARG_QUERYCURRENTFENCE structure](ns-d3dkmddi--dxgkarg-querycurrentfence.md) | The DXGKARG_QUERYCURRENTFENCE structure describes the latest completed submission fence. |
| [DXGK_MULTIPLANEOVERLAYCAPS structure](ns-d3dkmddi--dxgk-multiplaneoverlaycaps.md) | Multiplane overlay capabilities returned by the DxgkDdiGetMultiPlaneOverlayCaps function. |
| [DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 structure](ns-d3dkmddi--dxgkarg-setvidpnsourceaddresswithmultiplaneoverlay3.md) | Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3 function. |
| [DXGK_PRIMARYCONTEXTDATA structure](ns-d3dkmddi--dxgk-primarycontextdata.md) | TBD |
| [DXGK_PAGETABLEUPDATEADDRESS structure](ns-d3dkmddi--dxgk-pagetableupdateaddress.md) | DXGK_PAGETABLEUPDATEADDRESS contains the address of a page table to update. The member containing the address is defined as part of a DxgkDdiBuildPagingBuffer operation in the DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE structure. |
| [DXGK_POWER_RUNTIME_COMPONENT structure](ns-d3dkmddi--dxgk-power-runtime-component.md) | Describes information about a power component&#8212;for example, a graphics processing engine, a display device, or a block of memory. |
| [DXGKARG_SETVIDPNSOURCEADDRESS structure](ns-d3dkmddi--dxgkarg-setvidpnsourceaddress.md) | The DXGKARG_SETVIDPNSOURCEADDRESS structure contains arguments for the DxgkDdiSetVidPnSourceAddress function. |
| [DXGK_SEGMENTFLAGS structure](ns-d3dkmddi--dxgk-segmentflags.md) | The DXGK_SEGMENTFLAGS structure identifies properties for a segment that the driver provides through a call to its DxgkDdiQueryAdapterInfo function. |
| [DXGKARGCB_ENUMHANDLECHILDREN structure](ns-d3dkmddi--dxgkargcb-enumhandlechildren.md) | The DXGKARGCB_ENUMHANDLECHILDREN structure describes a parent resource and the index of one of its child allocations. |
| [DXGKARG_CREATEOVERLAY structure](ns-d3dkmddi--dxgkarg-createoverlay.md) | The DXGKARG_CREATEOVERLAY structure describes parameters to create an overlay. |
| [DXGK_DMABUFFERCAPS_DEPRECATED structure](ns-d3dkmddi--dxgk-dmabuffercaps-deprecated.md) | TBD |
| [DXGK_MULTIPLANE_OVERLAY_PLANE2 structure](ns-d3dkmddi--dxgk-multiplane-overlay-plane2.md) | DXGK_MULTIPLANE_OVERLAY_PLANE2 is used with the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to specify an overlay plane to display. |
| [DXGK_HWCONTEXT_CAPS structure](ns-d3dkmddi--dxgk-hwcontext-caps.md) | TBD |
| [DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO structure](ns-d3dkmddi-dxgk-check-multiplane-overlay-support-return-info.md) | Specifies limitations on hardware support of multiplane overlays. |
| [DXGK_CONTEXTINFO structure](ns-d3dkmddi--dxgk-contextinfo.md) | The DXGK_CONTEXTINFO structure describes a device context. |
| [DXGK_CONNECTION_CHANGE structure](ns-d3dkmddi--dxgk-connection-change.md) | Structure to describe the most recently updated status of the link for a target. |
| [DXGK_TRANSFERVIRTUALFLAGS structure](ns-d3dkmddi--dxgk-transfervirtualflags.md) | DXGK_TRANSFERVIRTUALFLAGS is used as part of an allocation transfer operation. |
| [DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 structure](ns-d3dkmddi--dxgkarg-checkmultiplaneoverlaysupport3.md) | Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for multi-plane overlays. |
| [DXGKARG_MAPCPUHOSTAPERTURE structure](ns-d3dkmddi--dxgkarg-mapcpuhostaperture.md) | The DXGKARG_MAPCPUHOSTAPERTURE structure is used to map an allocation, resident in a local memory segment, into the CPU host aperture in order to make it visible to the CPU. |
| [DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure](ns-d3dkmddi--dxgkcb-notify-interrupt-data-flags.md) | The DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS structure indicates whether the display miniport driver provides a physical adapter mask in a call to the DxgkCbNotifyInterrupt function. |
| [DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_WITH_SOURCE structure](ns-d3dkmddi--dxgk-multiplane-overlay-post-composition-with-source.md) | Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for post composition transform support. |
| [DXGKARG_SUBMITCOMMANDTOHWQUEUE structure](ns-d3dkmddi--dxgkarg-submitcommandtohwqueue.md) | TBD |
| [DXGK_MAPAPERTUREFLAGS structure](ns-d3dkmddi--dxgk-mapapertureflags.md) | The DXGK_MAPAPERTUREFLAGS structure identifies the type of map-aperture-segment operation to set up in a call to the DxgkDdiBuildPagingBuffer function. |
| [DXGKARG_FORMATHISTORYBUFFER structure](ns-d3dkmddi--dxgkarg-formathistorybuffer.md) | Contains info for the display miniport driver to format a history buffer. |
| [DXGK_MONITOR_INTERFACE structure](ns-d3dkmddi--dxgk-monitor-interface.md) | TBD |
| [DXGKARG_QUERYCONNECTIONCHANGE structure](ns-d3dkmddi--dxgkarg-queryconnectionchange.md) | Used to hold the arguments for DXGKDDI_QUERYCONNECTIONCHANGE. |
| [DXGK_GPUMMUCAPS structure](ns-d3dkmddi--dxgk-gpummucaps.md) | The DXGK_GPUMMUCAPS structure is used by the kernel mode driver to express virtual memory addressing capabilities. |
| [DXGKARG_CANCELCOMMAND structure](ns-d3dkmddi--dxgkarg-cancelcommand.md) | Specifies internal resources that are cleaned up by the DxgkDdiCancelCommand function after a command is removed from the hardware queue. |
| [DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO structure](ns-d3dkmddi--dxgk-multiplane-overlay-vsync-info.md) | Specifies an overlay plane to display during a VSync interval. |
| [DXGKARG_SETTIMINGSFROMVIDPN structure](ns-d3dkmddi--dxgkarg-settimingsfromvidpn.md) | Used to hold the arguments for DXGKDDI_SETTIMINGSFROMVIDPN. |
| [DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 structure](ns-d3dkmddi--dxgkarg-setvidpnsourceaddresswithmultiplaneoverlay2.md) | DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed.DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed. |
| [DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL structure](ns-d3dkmddi--dxgk-buildpagingbuffer-fillvirtual.md) | DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL is used as part of an operation to fill an allocation with a pattern. |
| [DXGK_DISCARDCONTENTFLAGS structure](ns-d3dkmddi--dxgk-discardcontentflags.md) | The DXGK_DISCARDCONTENTFLAGS structure identifies the type of discard-content operation to set up in a call to the DxgkDdiBuildPagingBuffer function. |
| [DXGKARG_CREATEDEVICE structure](ns-d3dkmddi--dxgkarg-createdevice.md) | The DXGKARG_CREATEDEVICE structure describes a graphics context device. |
| [DXGK_COLORTRANSFORMCAPS structure](ns-d3dkmddi--dxgk-colortransformcaps.md) | TBD |
| [DXGK_VIDPNSOURCEMODESET_INTERFACE structure](ns-d3dkmddi--dxgk-vidpnsourcemodeset-interface.md) | The DXGK_VIDPNSOURCEMODESET_INTERFACE structure contains pointers to functions that belong to the VidPn Source Mode Set interface, which is implemented by the video present network (VidPN) manager. |
| [DXGK_PRESENTFLAGS structure](ns-d3dkmddi--dxgk-presentflags.md) | The DXGK_PRESENTFLAGS structure identifies, in bit-field flags, the type of present operation to perform. |
| [DXGK_MULTIPLANE_OVERLAY_PLANE3 structure](ns-d3dkmddi--dxgk-multiplane-overlay-plane3.md) | Specifies an overlay plane to display in a call to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3 function. |
| [DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS structure](ns-d3dkmddi--dxgk-setvidpnsourceaddress-input-flags.md) | A structure containing the set of flags needed to set the VidPN source address. |
| [DXGK_INHERITED_TIMING_INFO structure](ns-d3dkmddi--dxgk-inherited-timing-info.md) | Structure passed to the driver in the pPrivateDriverData argument of DxgkDdiRecommendFunctionalVidPn, which the driver should use to describe the color space and wire format which cannot be described easily in the VidPn the DDI builds. |
| [DXGK_CREATECONTEXTFLAGS structure](ns-d3dkmddi--dxgk-createcontextflags.md) | The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts. |
| [DXGK_VIDPNTOPOLOGY_INTERFACE structure](ns-d3dkmddi--dxgk-vidpntopology-interface.md) | The DXGK_VIDPNTOPOLOGY_INTERFACE structure contains pointers to functions that belong to the VidPn Topology interface, which is implemented by the video present network (VidPN) manager. |
| [DXGKARG_CONTROLINTERRUPT2 structure](ns-d3dkmddi--dxgkarg-controlinterrupt2.md) | The DXGKARG_CONTROLINTERRUPT2 structure is used in DxgkDdi_ControlInterrupt2 calls to describe the state of interrupts. |
| [DXGKARG_GETMULTIPLANEOVERLAYCAPS structure](ns-d3dkmddi--dxgkarg-getmultiplaneoverlaycaps.md) | Arguments to the DxgkDdiGetMultiPlaneOverlayCaps function. |
| [DXGKARG_SETPOINTERPOSITION structure](ns-d3dkmddi--dxgkarg-setpointerposition.md) | The DXGKARG_SETPOINTERPOSITION structure describes where and how to display the mouse pointer. |
| [DXGK_PLANE_SPECIFIC_INPUT_FLAGS structure](ns-d3dkmddi--dxgk-plane-specific-input-flags.md) | A structure containing the input flags to be used for the driver that apply to a plane. |
| [DXGK_QUERYSEGMENTIN structure](ns-d3dkmddi--dxgk-querysegmentin.md) | The DXGK_QUERYSEGMENTIN structure describes relevant information for a memory-segment query through a call to the display miniport driver's DxgkDdiQueryAdapterInfo function. |
| [DXGK_SEGMENTBANKPREFERENCE structure](ns-d3dkmddi--dxgk-segmentbankpreference.md) | The DXGK_SEGMENTBANKPREFERENCE structure describes bank preferences for paging in an allocation. |
| [DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE structure](ns-d3dkmddi--dxgkargcb-reservegpuvirtualaddressrange.md) | DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE is used with the DxgkCbReserveGpuVirtualAddressRangedevice driver interface (DDI) to allow the kernel mode driver to reserve a graphics processing unit (GPU) virtual address range during creation of a process. |
| [DXGK_VIRTUALADDRESSCAPS_DEPRECATED structure](ns-d3dkmddi--dxgk-virtualaddresscaps-deprecated.md) | TBD |
| [DXGKARG_QUERYENGINESTATUS structure](ns-d3dkmddi--dxgkarg-queryenginestatus.md) | Used in a call to the DxgkDdiQueryEngineStatus function to specify a node within an active physical adapter (engine) that is to be queried for its progress. |
| [DXGKARGCB_PROTECTEDSESSIONSTATUS structure](ns-d3dkmddi--dxgkargcb-protectedsessionstatus.md) | Used for information on the status of the protected session. |
| [DXGKARG_CREATEHWCONTEXT structure](ns-d3dkmddi--dxgkarg-createhwcontext.md) | TBD |
| [DXGKARG_FLIPOVERLAY structure](ns-d3dkmddi--dxgkarg-flipoverlay.md) | The DXGKARG_FLIPOVERLAY structure describes a new allocation to display for the overlay. |
| [DXGKARG_CREATECONTEXT structure](ns-d3dkmddi--dxgkarg-createcontext.md) | The DXGKARG_CREATECONTEXT structure describes parameters to create a device context. |
| [DXGK_MULTIPLANE_OVERLAY_BLEND structure](ns-d3dkmddi--dxgk-multiplane-overlay-blend.md) | Identifies a blend operation to be performed on an overlay plane. |
| [DXGK_CPUHOSTAPERTURE structure](ns-d3dkmddi--dxgk-cpuhostaperture.md) | DXGK_CPUHOSTAPERTURE describes a memory segment supporting a CPU host aperture. |
| [DXGKARG_CREATEPROTECTEDSESSION structure](ns-d3dkmddi--dxgkarg-createprotectedsession.md) | Used to create a protected session. |
| [DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure](ns-d3dkmddi--dxgkarg-updateactivevidpnpresentpath.md) | The DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure contains a D3DKMDT_VIDPN_PRESENT_PATH structure, which contains arguments for the DxgkDdiUpdateActiveVidPnPresentPath function. |
| [DXGK_ALLOCATIONINFO structure](ns-d3dkmddi--dxgk-allocationinfo.md) | The DXGK_ALLOCATIONINFO structure describes parameters for creating an allocation. |
| [DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS structure](ns-d3dkmddi--dxgk-multiplane-overlay-ycbcr-flags.md) | Identifies YUV range and conversion info that describes a multiplane overlay. |
| [DXGK_OVERLAYINFO structure](ns-d3dkmddi--dxgk-overlayinfo.md) | The DXGK_OVERLAYINFO structure describes parameters that are required to create or modify an overlay. |
| [DXGKCB_GETHANDLEDATAFLAGS structure](ns-d3dkmddi--dxgkcb-gethandledataflags.md) | The DXGKCB_GETHANDLEDATAFLAGS structure indicates if allocations belong to a resource. |
| [DXGKARG_ESCAPE structure](ns-d3dkmddi--dxgkarg-escape.md) | The DXGKARG_ESCAPE structure describes information that the user-mode display driver shares with the display miniport driver. |
| [DXGK_MEMORYRANGE structure](ns-d3dkmddi--dxgk-memoryrange.md) | DXGK_MEMORYRANGE is used with DxgkDdiQueryAdapterInfo and DXGK_QUERYSEGMENTMEMORYSTATE to query bad graphics processing unit (GPU) memory ranges. |
| [DXGK_MONITORLINKINFO structure](ns-d3dkmddi--dxgk-monitorlinkinfo.md) | This structure was defined in WDDM 2.1, however the usage hints and capabilities structure definitions were nested within DXGK_MONITORLINKINFO. |
| [DXGKARG_CONTROLMODEBEHAVIOR structure](ns-d3dkmddi--dxgkarg-controlmodebehavior.md) | TBD |
| [DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE structure](ns-d3dkmddi--dxgk-multiplane-overlay-plane-with-source.md) | DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE describes the multi-plane overlay plane attributes, allocation, and video present network source identification number. |
| [DXGKARG_DESTROYPERIODICFRAMENOTIFICATION structure](ns-d3dkmddi--dxgkarg-destroyperiodicframenotification.md) | The arguments used to destroy a periodic frame notification. |
| [DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_FLAGS structure](ns-d3dkmddi--dxgk-multiplane-overlay-post-composition-flags.md) | A structure containing the flags describing the transformations applied to an image. |
| [DXGK_OPENALLOCATIONFLAGS structure](ns-d3dkmddi--dxgk-openallocationflags.md) | The DXGK_OPENALLOCATIONFLAGS structure identifies the operation to perform for allocations. |
| [DXGKARG_UNMAPCPUHOSTAPERTURE structure](ns-d3dkmddi--dxgkarg-unmapcpuhostaperture.md) | The DXGKARG_UNMAPCPUHOSTAPERTURE structure is used to unmap a previously mapped range of the CPU host aperture. |
| [DXGK_POWER_COMPONENT_INDEX structure](ns-d3dkmddi--dxgk-power-component-index.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [DXGKDDI_VIDPNTARGETMODESET_ACQUIREFIRSTMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirefirstmodeinfo.md) | The pfnAcquireFirstModeInfo function returns a descriptor of the first mode in a specified VidPN target mode set. |
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 callback function](nc-d3dkmddi-dxgkddi-setvidpnsourceaddresswithmultiplaneoverlay3.md) | TBD |
| [DXGKDDI_SETPALETTE callback function](nc-d3dkmddi-dxgkddi-setpalette.md) | TBD |
| [DXGKDDI_CREATECONTEXT callback function](nc-d3dkmddi-dxgkddi-createcontext.md) | TBD |
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 callback function](nc-d3dkmddi-dxgkddi-setvidpnsourceaddresswithmultiplaneoverlay2.md) | TBD |
| [DXGKDDI_CALIBRATEGPUCLOCK callback function](nc-d3dkmddi-dxgkddi-calibrategpuclock.md) | TBD |
| [DXGKDDI_DISPLAYDETECTCONTROL callback](nc-d3dkmddi-dxgkddi-displaydetectcontrol.md) | Used to turn hot plug detection on and off and to initiate status polls on either a specific target or all targets. |
| [DXGKDDI_VIDPNTOPOLOGY_RELEASEPATHINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md) | The pfnReleasePathInfo function releases a D3DKMDT_VIDPN_PRESENT_PATH structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKDDI_DESTROYHWCONTEXT callback function](nc-d3dkmddi-dxgkddi-destroyhwcontext.md) | TBD |
| [DXGKDDI_VIDPN_CREATENEWTARGETMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-createnewtargetmodeset.md) | The pfnCreateNewTargetModeSet function creates a new target mode set object within a specified VidPN object. |
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback](nc-d3dkmddi-dxgkddi-checkmultiplaneoverlaysupport.md) | Called by the Microsoft DirectX graphics kernel subsystem to check the details of hardware support for multiplane overlays. |
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 callback function](nc-d3dkmddi-dxgkddi-checkmultiplaneoverlaysupport3.md) | TBD |
| [DXGKDDI_MONITORSOURCEMODESET_CREATENEWMODEINFO callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-createnewmodeinfo.md) | The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_MONITOR_SOURCE_MODE structure that the display miniport driver populates before calling pfnAddMode. |
| [DXGKDDI_SETROOTPAGETABLE callback function](nc-d3dkmddi-dxgkddi-setrootpagetable.md) | TBD |
| [DXGKDDI_ESCAPE callback function](nc-d3dkmddi-dxgkddi-escape.md) | TBD |
| [DXGKDDI_RELEASESWIZZLINGRANGE callback function](nc-d3dkmddi-dxgkddi-releaseswizzlingrange.md) | TBD |
| [DXGKDDI_RECOMMENDFUNCTIONALVIDPN callback function](nc-d3dkmddi-dxgkddi-recommendfunctionalvidpn.md) | TBD |
| [DXGKDDI_PRESENTDISPLAYONLY callback function](nc-d3dkmddi-dxgkddi-presentdisplayonly.md) | TBD |
| [DXGKDDI_CLOSEALLOCATION callback function](nc-d3dkmddi-dxgkddi-closeallocation.md) | TBD |
| [DXGKCB_DXGKCB_MITIGATEDRANGEUPDATE callback function](nc-d3dkmddi-dxgkcb-dxgkcb-mitigatedrangeupdate.md) | TBD |
| [DXGKDDI_VIDPNSOURCEMODESET_GETNUMMODES callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-getnummodes.md) | The pfnGetNumModes function returns the number of source modes in a specified VidPN source mode set. |
| [DXGKCB_GETHANDLEPARENT callback](nc-d3dkmddi-dxgkcb-gethandleparent.md) | The DxgkCbGetHandleParent function retrieves the parent resource from the specified allocation. |
| [DXGKDDI_SETVIDPNSOURCEVISIBILITY callback function](nc-d3dkmddi-dxgkddi-setvidpnsourcevisibility.md) | TBD |
| [DXGKDDI_VIDPN_RELEASETARGETMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-releasetargetmodeset.md) | The pfnReleaseTargetModeSet function releases a handle to a target mode set object. |
| [DXGKDDI_VIDPNSOURCEMODESET_ACQUIREPINNEDMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirepinnedmodeinfo.md) | The pfnAcquirePinnedModeInfo function returns a descriptor of the pinned mode in a specified VidPN source mode set. |
| [DXGKDDI_UPDATEHWCONTEXTSTATE callback function](nc-d3dkmddi-dxgkddi-updatehwcontextstate.md) | TBD |
| [DXGKDDI_RENDER callback function](nc-d3dkmddi-dxgkddi-render.md) | TBD |
| [DXGKDDI_MONITOR_GETADDITIONALMONITORMODESET callback](nc-d3dkmddi-dxgkddi-monitor-getadditionalmonitormodeset.md) | The pfnGetAdditionalMonitorModeSet function, available in the DXGK_MONITOR_INTERFACE_V2 interface beginning with Windows 7, returns a handle to an additional monitor source mode set object that is associated with a specified monitor. |
| [DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY callback function](nc-d3dkmddi-dxgkddi-setvidpnsourceaddresswithmultiplaneoverlay.md) | TBD |
| [DXGKDDISETPOWERPSTATE callback function](nc-d3dkmddi-dxgkddisetpowerpstate.md) | TBD |
| [DXGKDDI_CONTROLMODEBEHAVIOR callback function](nc-d3dkmddi-dxgkddi-controlmodebehavior.md) | TBD |
| [DXGKDDI_DESTROYPROTECTEDSESSION callback function](nc-d3dkmddi-dxgkddi-destroyprotectedsession.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-updatepathsupportinfo.md) | The pfnUpdatePathSupportInfo function updates the transformation and copy protection support of a particular path in a specified VidPN topology. |
| [DXGKDDI_VIDPNTARGETMODESET_ACQUIREPINNEDMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirepinnedmodeinfo.md) | The pfnAcquirePinnedModeInfo function returns a descriptor of the pinned mode in a specified VidPN target mode set. |
| [DXGKDDI_VIDPNSOURCEMODESET_ACQUIREFIRSTMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirefirstmodeinfo.md) | The pfnAcquireFirstModeInfo function returns a descriptor of the first mode in a specified VidPN source mode set. |
| [DXGKDDI_CREATEPROTECTEDSESSION callback function](nc-d3dkmddi-dxgkddi-createprotectedsession.md) | TBD |
| [DXGKDDI_SETTIMINGSFROMVIDPN callback function](nc-d3dkmddi-dxgkddi-settimingsfromvidpn.md) | TBD |
| [DXGKDDI_VIDPNTARGETMODESET_ACQUIRENEXTMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-acquirenextmodeinfo.md) | The pfnAcquireNextModeInfo function returns a descriptor of the next mode in a specified VidPN target mode set, given the current mode. |
| [DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES callback](nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-getnumfrequencyranges.md) | The pfnGetNumFrequencyRanges returns the number of frequency range descriptors in a specified monitor frequency range set object. |
| [DXGKDDI_GETSTANDARDALLOCATIONDRIVERDATA callback function](nc-d3dkmddi-dxgkddi-getstandardallocationdriverdata.md) | TBD |
| [DXGKDDI_SETTARGETANALOGCOPYPROTECTION callback](nc-d3dkmddi-dxgkddi-settargetanalogcopyprotection.md) | Sets the analog copy protection on the specified target id. This is functionally equivalent to the DxgkDdiUpdateActiveVidPnPresentPath in previous WDDM versions if only the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION is changed. |
| [DXGKDDI_MONITOR_GETMONITORFREQUENCYRANGESET callback](nc-d3dkmddi-dxgkddi-monitor-getmonitorfrequencyrangeset.md) | The pfnGetMonitorFrequencyRangeSet function returns a handle to the monitor frequency range set object that is associated with a specified monitor. |
| [DXGKDDI_BUILDPAGINGBUFFER callback function](nc-d3dkmddi-dxgkddi-buildpagingbuffer.md) | TBD |
| [DXGKDDI_CREATEALLOCATION callback function](nc-d3dkmddi-dxgkddi-createallocation.md) | TBD |
| [DXGKDDI_MONITORSOURCEMODESET_RELEASEMODEINFO callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-releasemodeinfo.md) | The pfnReleaseModeInfo function releases a D3DKMDT_MONITOR_SOURCE_MODE structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS callback](nc-d3dkmddi-dxgkddi-monitordescriptorset-getnumdescriptors.md) | The pfnGetNumDescriptors function returns the number of descriptors in a monitor descriptor set. |
| [DXGKDDI_VIDPNTOPOLOGY_ADDPATH callback](nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md) | The pfnAddPath function adds a video present path to a specified VidPN topology object. |
| [DXGKCB_GETCAPTUREADDRESS callback](nc-d3dkmddi-dxgkcb-getcaptureaddress.md) | The DxgkCbGetCaptureAddress function retrieves the physical address and segment identifier of a capture buffer that is associated with the given allocation handle. |
| [DXGKDDI_CREATEPERIODICFRAMENOTIFICATION callback](nc-d3dkmddi-dxgkddi-createperiodicframenotification.md) | Used to create a periodic frame notification. |
| [DXGKDDI_CONTROLINTERRUPT2 callback](nc-d3dkmddi-dxgkddi-controlinterrupt2.md) | The DxgkDdi_ControlInterrupt2 function enables or disables the given interrupt type on the graphics hardware. |
| [DXGKDDI_UPDATEOVERLAY callback function](nc-d3dkmddi-dxgkddi-updateoverlay.md) | TBD |
| [DXGKDDI_RESETENGINE callback function](nc-d3dkmddi-dxgkddi-resetengine.md) | TBD |
| [DXGKDDI_MONITOR_ACQUIREMONITORSOURCEMODESET callback](nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md) | The pfnAcquireMonitorSourceModeSet function returns a handle to the monitor source mode set object that is associated with a specified monitor. |
| [DXGKDDI_VIDPN_RELEASESOURCEMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-releasesourcemodeset.md) | The pfnReleaseSourceModeSet function releases a handle to a source mode set object. |
| [DXGKDDI_ISSUPPORTEDVIDPN callback function](nc-d3dkmddi-dxgkddi-issupportedvidpn.md) | TBD |
| [DXGKDDI_VIDPNTARGETMODESET_GETNUMMODES callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-getnummodes.md) | The pfnGetNumModes function returns the number of target modes in a specified VidPN target mode set. |
| [DXGKDDI_QUERYCURRENTFENCE callback](nc-d3dkmddi-dxgkddi-querycurrentfence.md) | The DxgkDdiQueryCurrentFence function queries about the latest completed submission fence identifier in the hardware command execution unit. |
| [DXGKDDI_MONITORSOURCEMODESET_GETNUMMODES callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-getnummodes.md) | The pfnGetNumModes function returns the number modes in a specified monitor source mode set. |
| [DXGKCB_NOTIFY_DPC callback](nc-d3dkmddi-dxgkcb-notify-dpc.md) | The DxgkCbNotifyDpc function informs the graphics processing unit (GPU) scheduler about a graphics hardware update at deferred-procedure-call (DPC) time. |
| [DXGKDDI_DESCRIBEALLOCATION callback function](nc-d3dkmddi-dxgkddi-describeallocation.md) | TBD |
| [DXGKDDI_DESTROYALLOCATION callback function](nc-d3dkmddi-dxgkddi-destroyallocation.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHSFROMSOURCE callback](nc-d3dkmddi-dxgkddi-vidpntopology-getnumpathsfromsource.md) | The pfnGetNumPathsFromSource function returns the number of video present paths that contain a specified video present source. |
| [DXGKDDI_RESETHWENGINE callback function](nc-d3dkmddi-dxgkddi-resethwengine.md) | TBD |
| [DXGKDDI_VIDPNSOURCEMODESET_PINMODE callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-pinmode.md) | The pfnPinMode function pins a specified mode in a VidPN source mode set. |
| [DXGKDDI_SETPOINTERSHAPE callback function](nc-d3dkmddi-dxgkddi-setpointershape.md) | TBD |
| [DXGKDDI_QUERYVIDPNHWCAPABILITY callback function](nc-d3dkmddi-dxgkddi-queryvidpnhwcapability.md) | TBD |
| [DXGKDDI_SETTARGETCONTENTTYPE callback](nc-d3dkmddi-dxgkddi-settargetcontenttype.md) | Passes the content type for which the driver should optimize on the specified target. |
| [DXGKCB_DESTROYCONTEXTALLOCATION callback](nc-d3dkmddi-dxgkcb-destroycontextallocation.md) | Called by a WDDM 1.2 or later display miniport driver to free a resource that was previously allocated for a GPU or device-specific context. |
| [DXGKDDI_QUERYCONNECTIONCHANGE callback](nc-d3dkmddi-dxgkddi-queryconnectionchange.md) | The OS calls this in response to a status change reported through DxgkCbIndicateConnectorChange or when the OutputFlags.ConnectorStatusChanges field indicates that a call to SetTimingsFromVidPn has detected connector status changes. |
| [DXGKCB_COMPLETEPSTATETRANSITION callback](nc-d3dkmddi-dxgkcb-completepstatetransition.md) | Reserved for system use. Do not use it in your driver. |
| [DXGKDDI_RENDERKM callback function](nc-d3dkmddi-dxgkddi-renderkm.md) | TBD |
| [DXGKDDI_UNMAPCPUHOSTAPERTURE callback function](nc-d3dkmddi-dxgkddi-unmapcpuhostaperture.md) | TBD |
| [DXGKDDI_MONITORSOURCEMODESET_ADDMODE callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-addmode.md) | The pfnAddMode function adds a monitor source mode to a specified monitor source mode set object. |
| [DXGKDDI_MONITORSOURCEMODESET_ACQUIREPREFERREDMODEINFO callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-acquirepreferredmodeinfo.md) | The pfnAcquirePreferredModeInfo returns a descriptor of the preferred mode in a specified monitor source mode set object. |
| [DXGKDDI_VIDPN_ASSIGNTARGETMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-assigntargetmodeset.md) | The pfnAssignTargetModeSet function assigns a target mode set to a particular target in a specified VidPN. |
| [DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE callback](nc-d3dkmddi-dxgkddi-vidpntopology-enumpathtargetsfromsource.md) | The pfnEnumPathTargetsFromSource function returns the identifier of one of the video present targets associated with a specified video present source. |
| [DXGKCB_INDICATE_CONNECTOR_CHANGE callback](nc-d3dkmddi-dxgkcb-indicate-connector-change.md) | DXGKCB_INDICATE_CONNECTOR_CHANGE is called by the KMD to indicate that it has added changes to its change queue which the OS should now query. |
| [DXGKDDI_CANCELCOMMAND callback function](nc-d3dkmddi-dxgkddi-cancelcommand.md) | TBD |
| [DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET callback](nc-d3dkmddi-dxgkddi-monitor-releasemonitorsourcemodeset.md) | The pfnReleaseMonitorSourceModeSet function releases a handle to a monitor source mode set object. |
| [DXGKDDI_PREEMPTCOMMAND callback function](nc-d3dkmddi-dxgkddi-preemptcommand.md) | TBD |
| [DXGKCB_SETPOWERCOMPONENTRESIDENCY callback](nc-d3dkmddi-dxgkcb-setpowercomponentresidency.md) | Called by the display miniport driver to set the expected residency for a power component of type DXGK_POWER_COMPONENT_OTHER. |
| [DXGKDDI_CREATEOVERLAY callback function](nc-d3dkmddi-dxgkddi-createoverlay.md) | TBD |
| [DXGKDDI_COLLECTDBGINFO callback function](nc-d3dkmddi-dxgkddi-collectdbginfo.md) | TBD |
| [DXGKDDI_DESTROYCONTEXT callback function](nc-d3dkmddi-dxgkddi-destroycontext.md) | TBD |
| [DXGKDDI_VIDPN_GETTOPOLOGY callback](nc-d3dkmddi-dxgkddi-vidpn-gettopology.md) | The pfnGetTopology function returns a handle to the VidPN topology object contained by a specified VidPN object. |
| [DXGKCB_UPDATECONTEXTALLOCATION callback](nc-d3dkmddi-dxgkcb-updatecontextallocation.md) | DxgkCbUpdateContextAllocation is used to update the content of a context allocation. |
| [DXGKDDI_RECOMMENDVIDPNTOPOLOGY callback function](nc-d3dkmddi-dxgkddi-recommendvidpntopology.md) | TBD |
| [DXGKDDI_GETROOTPAGETABLESIZE callback function](nc-d3dkmddi-dxgkddi-getrootpagetablesize.md) | TBD |
| [DXGKDDI_SUBMITCOMMANDTOHWQUEUE callback function](nc-d3dkmddi-dxgkddi-submitcommandtohwqueue.md) | TBD |
| [DXGKCB_COMPLETEFSTATETRANSITION callback](nc-d3dkmddi-dxgkcb-completefstatetransition.md) | Called by a Windows Display Driver Model (WDDM) 1.2 or later display miniport driver to notify the port driver that a power component has completed the F-state transition. |
| [DXGKCB_MAPCONTEXTALLOCATION callback](nc-d3dkmddi-dxgkcb-mapcontextallocation.md) | Maps a graphics processing unit (GPU) virtual address to the specified context allocation. |
| [DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO callback](nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirefirstdescriptorinfo.md) | The pfnAcquireFirstDescriptorInfo function returns the first descriptor in a monitor descriptor set object. |
| [DXGKDDI_QUERYENGINESTATUS callback function](nc-d3dkmddi-dxgkddi-queryenginestatus.md) | TBD |
| [DXGKCB_NOTIFYVSYNC callback function](nc-d3dkmddi-dxgkcb-notifyvsync.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_ACQUIREFIRSTPATHINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-acquirefirstpathinfo.md) | The pfnAcquireFirstPathInfo structure returns a descriptor of the first path in a specified VidPN topology object. |
| [DXGKDDI_PRESENT callback function](nc-d3dkmddi-dxgkddi-present.md) | TBD |
| [DXGKDDI_GETNODEMETADATA callback](nc-d3dkmddi-dxgkddi-getnodemetadata.md) | From a provided adapter handle, returns the engine type and friendly name of an engine on a specified GPU node. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later display miniport drivers. |
| [DXGKCB_SETPOWERCOMPONENTACTIVE callback](nc-d3dkmddi-dxgkcb-setpowercomponentactive.md) | Called by the display miniport driver to access a power component. |
| [DXGKDDI_STOPCAPTURE callback function](nc-d3dkmddi-dxgkddi-stopcapture.md) | TBD |
| [DXGKDDI_VIDPN_CREATENEWSOURCEMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md) | The pfnCreateNewSourceModeSet function creates a new source mode set object within a specified VidPN object. |
| [DXGKDDI_VIDPN_ACQUIRETARGETMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md) | The pfnAcquireTargetModeSet function returns a handle to a particular target mode set object that is contained by a specified VidPN object. |
| [DXGKDDI_MONITOR_RELEASEADDITIONALMONITORMODESET callback](nc-d3dkmddi-dxgkddi-monitor-releaseadditionalmonitormodeset.md) | The pfnReleaseAdditionalMonitorModeSet function, available in the DXGK_MONITOR_INTERFACE_V2 interface beginning with Windows 7, releases a handle to an additional monitor source mode set object that is associated with a specified monitor. |
| [DXGKDDI_VIDPN_ACQUIRESOURCEMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md) | The pfnAcquireSourceModeSet function returns a handle to a particular source mode set object that is contained by a specified VidPN object. |
| [DXGKCB_CREATECONTEXTALLOCATION callback](nc-d3dkmddi-dxgkcb-createcontextallocation.md) | Called by a Windows Display Driver Model (WDDM) 1.2 or later display miniport driver to allocate a GPU context or device-specific context. |
| [DXGKDDI_SETPOINTERPOSITION callback function](nc-d3dkmddi-dxgkddi-setpointerposition.md) | TBD |
| [DXGKDDI_VIDPNSOURCEMODESET_CREATENEWMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-createnewmodeinfo.md) | The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_VIDPN_SOURCE_MODE structure that the display miniport driver populates before calling pfnAddMode. |
| [DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO callback function](nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-acquirenextfrequencyrangeinfo.md) | TBD |
| [DXGKDDI_VIDPN_ASSIGNMULTISAMPLINGMETHODSET callback](nc-d3dkmddi-dxgkddi-vidpn-assignmultisamplingmethodset.md) | The pfnAssignMultisamplingMethodSet function assigns a set of multisampling methods to a particular video present source in a specified VidPN. |
| [DXGKDDI_SUBMITCOMMANDVIRTUAL callback function](nc-d3dkmddi-dxgkddi-submitcommandvirtual.md) | TBD |
| [DXGKCB_RESERVEGPUVIRTUALADDRESSRANGE callback](nc-d3dkmddi-dxgkcb-reservegpuvirtualaddressrange.md) | DxgkCbReserveGpuVirtualAddressRange allows the kernel mode driver to reserve a graphics processing unit (GPU) virtual address range during creation of a process. |
| [DXGKDDI_DESTROYPROCESS callback function](nc-d3dkmddi-dxgkddi-destroyprocess.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-createnewpathinfo.md) | The pfnCreateNewPathInfo function returns a pointer to a D3DKMDT_VIDPN_PRESENT_PATH structure that the display miniport driver populates before calling pfnAddPath. |
| [DXGKDDI_SETSTABLEPOWERSTATE callback function](nc-d3dkmddi-dxgkddi-setstablepowerstate.md) | TBD |
| [DXGKDDI_CREATEPROCESS callback function](nc-d3dkmddi-dxgkddi-createprocess.md) | TBD |
| [DXGKCB_RELEASEHANDLEDATA callback function](nc-d3dkmddi-dxgkcb-releasehandledata.md) | TBD |
| [DXGKDDI_SWITCHTOHWCONTEXTLIST callback function](nc-d3dkmddi-dxgkddi-switchtohwcontextlist.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS callback](nc-d3dkmddi-dxgkddi-vidpntopology-getnumpaths.md) | The pfnGetNumPaths function returns the number of video present paths in a specified VidPN topology. |
| [DXGKDDI_QUERYDEPENDENTENGINEGROUP callback function](nc-d3dkmddi-dxgkddi-querydependentenginegroup.md) | TBD |
| [DXGKDDI_VIDPNTARGETMODESET_ADDMODE callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-addmode.md) | The pfnAddMode function adds a VidPN target mode to a specified VidPN target mode set object. |
| [DXGKDDI_GETPOSTCOMPOSITIONCAPS callback function](nc-d3dkmddi-dxgkddi-getpostcompositioncaps.md) | TBD |
| [DXGKDDI_DESTROYOVERLAY callback function](nc-d3dkmddi-dxgkddi-destroyoverlay.md) | TBD |
| [DXGKDDI_VIDPN_ASSIGNSOURCEMODESET callback](nc-d3dkmddi-dxgkddi-vidpn-assignsourcemodeset.md) | The pfnAssignSourceModeSet function assigns a source mode set to a particular source in a specified VidPN. |
| [DXGKDDI_MAPCPUHOSTAPERTURE callback function](nc-d3dkmddi-dxgkddi-mapcpuhostaperture.md) | TBD |
| [DXGKDDI_CONTROLINTERRUPT callback function](nc-d3dkmddi-dxgkddi-controlinterrupt.md) | TBD |
| [DXGKDDI_QUERYADAPTERINFO callback function](nc-d3dkmddi-dxgkddi-queryadapterinfo.md) | TBD |
| [DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO callback](nc-d3dkmddi-dxgkddi-monitordescriptorset-releasedescriptorinfo.md) | The pfnReleaseDescriptorInfo function releases a D3DKMDT_MONITOR_DESCRIPTOR structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKCB_POWERRUNTIMECONTROLREQUEST callback](nc-d3dkmddi-dxgkcb-powerruntimecontrolrequest.md) | Called by the display miniport driver to exchange information with the Power Engine Plug-in (PEP). |
| [DXGKDDI_PATCH callback function](nc-d3dkmddi-dxgkddi-patch.md) | TBD |
| [DXGKDDI_SETTARGETGAMMA callback](nc-d3dkmddi-dxgkddi-settargetgamma.md) | Allows the gamma LUT to be set on a path which is identified by the target id.Note  This is functionally equivalent to the DxgkDdi_UpdateActiveVidPnPresentPath in previous WDDM versions if only the D3DKMDT_GAMMA_RAMP field is changed. . |
| [DXGKDDI_MONITORSOURCEMODESET_ACQUIREFIRSTMODEINFO callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-acquirefirstmodeinfo.md) | The pfnAcquireFirstModeInfo function returns a descriptor of the first mode in a specified monitor source mode set. |
| [DXGKDDI_VIDPNTARGETMODESET_PINMODE callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-pinmode.md) | The pfnPinMode function pins a specified mode in a VidPN target mode set. |
| [DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES callback function](nc-d3dkmddi-dxgkcb-unblockuefiframebufferranges.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_ACQUIREPATHINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-acquirepathinfo.md) | The pfnAcquirePathInfo function returns a descriptor of the video present path specified by a video present source and a video present target within a particular VidPN topology. |
| [DXGKCB_SETPROTECTEDSESSIONSTATUS callback function](nc-d3dkmddi-dxgkcb-setprotectedsessionstatus.md) | TBD |
| [DXGKDDI_FLIPOVERLAY callback function](nc-d3dkmddi-dxgkddi-flipoverlay.md) | TBD |
| [DXGKDDI_RESTARTFROMTIMEOUT callback function](nc-d3dkmddi-dxgkddi-restartfromtimeout.md) | TBD |
| [DXGKDDI_FORMATHISTORYBUFFER callback function](nc-d3dkmddi-dxgkddi-formathistorybuffer.md) | TBD |
| [DXGKCB_GETHANDLEDATA callback](nc-d3dkmddi-dxgkcb-gethandledata.md) | The DxgkCbGetHandleData function retrieves the private data that is associated with an allocation. |
| [DXGKDDI_ENUMVIDPNCOFUNCMODALITY callback function](nc-d3dkmddi-dxgkddi-enumvidpncofuncmodality.md) | TBD |
| [DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET callback](nc-d3dkmddi-dxgkddi-monitor-getmonitordescriptorset.md) | The pfnGetMonitorDescriptorSet function returns a handle to a monitor descriptor set object that is associated with a specified monitor. |
| [DXGKCB_SETPOWERCOMPONENTLATENCY callback](nc-d3dkmddi-dxgkcb-setpowercomponentlatency.md) | Called by the display miniport driver to set the latency tolerance for a power component of type DXGK_POWER_COMPONENT_OTHER. |
| [DXGKDDI_POWERRUNTIMESETDEVICEHANDLE callback function](nc-d3dkmddi-dxgkddi-powerruntimesetdevicehandle.md) | TBD |
| [DXGKDDI_VIDPNSOURCEMODESET_RELEASEMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-releasemodeinfo.md) | The pfnReleaseModeInfo function releases a D3DKMDT_VIDPN_SOURCE_MODE structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKDDI_VIDPNTARGETMODESET_CREATENEWMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-createnewmodeinfo.md) | The pfnCreateNewModeInfo function returns a pointer to a D3DKMDT_VIDPN_TARGET_MODE structure that the display miniport driver populates before calling pfnAddMode. |
| [DXGKDDI_COMMITVIDPN callback function](nc-d3dkmddi-dxgkddi-commitvidpn.md) | TBD |
| [DXGKDDI_ACQUIRESWIZZLINGRANGE callback function](nc-d3dkmddi-dxgkddi-acquireswizzlingrange.md) | TBD |
| [DXGKCB_MULTIPLANEOVERLAYDISABLED callback](nc-d3dkmddi-dxgkcb-multiplaneoverlaydisabled.md) | This callback allows the kernel mode driver to indicate that the current multiplane overlay configuration is no longer supported on the specified VidPnSourceId. |
| [DXGKCB_ENUMHANDLECHILDREN callback](nc-d3dkmddi-dxgkcb-enumhandlechildren.md) | The DxgkCbEnumHandleChildren function enumerates all of the allocations that are associated with a given resource, one allocation at a time. |
| [DXGKDDI_VIDPNTOPOLOGY_GETPATHSOURCEFROMTARGET callback](nc-d3dkmddi-dxgkddi-vidpntopology-getpathsourcefromtarget.md) | The pfnGetPathSourceFromTarget function returns the identifier of the video present source that is associated with a specified video present target. |
| [DXGKDDI_DESTROYDEVICE callback function](nc-d3dkmddi-dxgkddi-destroydevice.md) | TBD |
| [DXGKCB_ACQUIREHANDLEDATA callback function](nc-d3dkmddi-dxgkcb-acquirehandledata.md) | TBD |
| [DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT2 callback function](nc-d3dkmddi-dxgkddi-checkmultiplaneoverlaysupport2.md) | TBD |
| [DXGKCB_QUERYVIDPNINTERFACE callback](nc-d3dkmddi-dxgkcb-queryvidpninterface.md) | The DxgkCbQueryVidPnInterface function returns a pointer to a DXGK_VIDPN_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter a VidPN object. |
| [DXGKDDI_VIDPNTARGETMODESET_RELEASEMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpntargetmodeset-releasemodeinfo.md) | The pfnReleaseModeInfo function releases a D3DKMDT_VIDPN_TARGET_MODE structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKDDI_POSTMULTIPLANEOVERLAYPRESENT callback function](nc-d3dkmddi-dxgkddi-postmultiplaneoverlaypresent.md) | TBD |
| [DXGKDDI_SUBMITCOMMAND callback function](nc-d3dkmddi-dxgkddi-submitcommand.md) | TBD |
| [DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH callback](nc-d3dkmddi-dxgkddi-vidpntopology-removepath.md) | The pfnRemovePath function removes a video present path to a specified VidPN topology object. |
| [DXGKDDI_SETVIDEOPROTECTEDREGION callback function](nc-d3dkmddi-dxgkddi-setvideoprotectedregion.md) | TBD |
| [DXGKDDI_UPDATEMONITORLINKINFO callback function](nc-d3dkmddi-dxgkddi-updatemonitorlinkinfo.md) | TBD |
| [DXGKDDI_GETSCANLINE callback function](nc-d3dkmddi-dxgkddi-getscanline.md) | TBD |
| [DXGKCB_QUERYMONITORINTERFACE callback](nc-d3dkmddi-dxgkcb-querymonitorinterface.md) | The DxgkCbQueryMonitorInterface function returns a pointer to a DXGK_MONITOR_INTERFACE structure. |
| [DXGKDDI_RESETFROMTIMEOUT callback function](nc-d3dkmddi-dxgkddi-resetfromtimeout.md) | TBD |
| [DXGKDDISETPOWERCOMPONENTFSTATE callback function](nc-d3dkmddi-dxgkddisetpowercomponentfstate.md) | TBD |
| [DXGKDDI_VALIDATEUPDATEALLOCATIONPROPERTY callback function](nc-d3dkmddi-dxgkddi-validateupdateallocationproperty.md) | TBD |
| [DXGKDDI_CREATEHWCONTEXT callback function](nc-d3dkmddi-dxgkddi-createhwcontext.md) | TBD |
| [DXGKCB_HARDWARECONTENTPROTECTIONTEARDOWN callback](nc-d3dkmddi-dxgkcb-hardwarecontentprotectionteardown.md) | DxgkCbHardwareContentProtectionTeardown is used to indicate when a hardware content protection event occurs. |
| [DXGKDDI_RENDERGDI callback function](nc-d3dkmddi-dxgkddi-rendergdi.md) | TBD |
| [DXGKDDIPOWERRUNTIMECONTROLREQUEST callback function](nc-d3dkmddi-dxgkddipowerruntimecontrolrequest.md) | TBD |
| [DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION callback](nc-d3dkmddi-dxgkddi-destroyperiodicframenotification.md) | Used to destroy a periodic frame notification. |
| [DXGKDDI_VIDPNTOPOLOGY_ACQUIRENEXTPATHINFO callback](nc-d3dkmddi-dxgkddi-vidpntopology-acquirenextpathinfo.md) | The pfnAcquireNextPathInfo function returns a descriptor of the next video present path in a specified VidPN topology, given the current path. |
| [DXGKDDI_CREATEDEVICE callback function](nc-d3dkmddi-dxgkddi-createdevice.md) | TBD |
| [DXGKCB_INVALIDATEHWCONTEXT callback function](nc-d3dkmddi-dxgkcb-invalidatehwcontext.md) | TBD |
| [DXGKDDI_UPDATEACTIVEVIDPNPRESENTPATH callback function](nc-d3dkmddi-dxgkddi-updateactivevidpnpresentpath.md) | TBD |
| [DXGKDDI_CREATEHWQUEUE callback function](nc-d3dkmddi-dxgkddi-createhwqueue.md) | TBD |
| [DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO callback](nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-releasefrequencyrangeinfo.md) | The pfnReleaseFrequencyRangeInfo function releases a D3DKMDT_MONITOR_FREQUENCY_RANGE structure that the VidPN manager previously provided to the display miniport driver. |
| [DXGKDDI_DESTROYHWQUEUE callback function](nc-d3dkmddi-dxgkddi-destroyhwqueue.md) | TBD |
| [DXGKDDI_VIDPNSOURCEMODESET_ADDMODE callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-addmode.md) | The pfnAddMode function adds a VidPN source mode to a specified VidPN source mode set object. |
| [DXGKDDI_VIDPNSOURCEMODESET_ACQUIRENEXTMODEINFO callback](nc-d3dkmddi-dxgkddi-vidpnsourcemodeset-acquirenextmodeinfo.md) | The pfnAcquireNextModeInfo function returns a descriptor of the next mode in a specified VidPN source mode set, given the current mode. |
| [DXGKCB_SETPOWERCOMPONENTIDLE callback](nc-d3dkmddi-dxgkcb-setpowercomponentidle.md) | Called by the display miniport driver to notify the Microsoft DirectX graphics kernel subsystem that a power component is no longer needed. |
| [DXGKDDI_GETMULTIPLANEOVERLAYCAPS callback function](nc-d3dkmddi-dxgkddi-getmultiplaneoverlaycaps.md) | TBD |
| [DXGKDDI_RECOMMENDMONITORMODES callback function](nc-d3dkmddi-dxgkddi-recommendmonitormodes.md) | TBD |
| [DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO callback](nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirenextdescriptorinfo.md) | The pfnAcquireNextDescriptorInfo function returns the next descriptor in a monitor descriptor set, given the current descriptor. |
| [DXGKCB_NOTIFY_INTERRUPT callback](nc-d3dkmddi-dxgkcb-notify-interrupt.md) | The DxgkCbNotifyInterrupt function informs the graphics processing unit (GPU) scheduler about a graphics hardware update at interrupt-service-routine (ISR) time. |
| [DXGKDDI_SETDISPLAYPRIVATEDRIVERFORMAT callback function](nc-d3dkmddi-dxgkddi-setdisplayprivatedriverformat.md) | TBD |
| [DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIREFIRSTFREQUENCYRANGEINFO callback function](nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-acquirefirstfrequencyrangeinfo.md) | TBD |
| [DXGKDDI_MONITORSOURCEMODESET_ACQUIRENEXTMODEINFO callback](nc-d3dkmddi-dxgkddi-monitorsourcemodeset-acquirenextmodeinfo.md) | The pfnAcquireNextModeInfo function returns a descriptor of the next mode in a specified monitor source mode set, given the current mode. |
| [DXGKDDI_OPENALLOCATIONINFO callback function](nc-d3dkmddi-dxgkddi-openallocationinfo.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DXGK_GDIROP_COLORFILL enumeration](ne-d3dkmddi--dxgk-gdirop-colorfill.md) | The DXGK_GDIROP_COLORFILL enumeration indicates the type of GDI raster operation (ROP) to implement in a GDI hardware-accelerated color fill operation. |
| [DXGK_POWER_COMPONENT_TYPE enumeration](ne-d3dkmddi--dxgk-power-component-type.md) | Indicates the power component type that is reported by the display miniport driver to the Microsoft DirectX graphics kernel subsystem. |
| [DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration](ne-d3dkmddi--dxgk-multiplane-overlay-stereo-flip-mode.md) | Identifies the overlay plane's stereo flip mode. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported. |
| [DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT enumeration](ne-d3dkmddi--dxgk-multiplane-overlay-video-frame-format.md) | Identifies the overlay plane's video frame format. Only the DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported. |
| [DXGK_INTERRUPT_TYPE enumeration](ne-d3dkmddi--dxgk-interrupt-type.md) | The DXGK_INTERRUPT_TYPE enumeration indicates the type of interrupt that the display miniport driver notifies the graphics processing unit (GPU) scheduler about. |
| [DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration](ne-d3dkmddi--dxgk-active-vidpn-invalidation-reason.md) | The DXGK_ACTIVE_VIDPN_INVALIDATION_REASON enumeration is used to indicate the reason why an active VidPN is invalidated and a new VidPN is requested. |
| [DXGK_DISPLAYDETECTCONTROLTYPE enumeration](ne-d3dkmddi--dxgk-displaydetectcontroltype.md) | Enumeration indicating the type of display detection action. |
| [DXGK_GLITCH_EFFECT enumeration](ne-d3dkmddi--dxgk-glitch-effect.md) | Enumeration which describes the user visible effect of a glitch during a SetTimingsFromVidPn call. |
| [DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration](ne-d3dkmddi--dxgk-multiplane-overlay-stereo-format.md) | Identifies the overlay plane's stereo presentation format. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported. |
| [DXGK_PATH_UPDATE enumeration](ne-d3dkmddi--dxgk-path-update.md) | Enum which indicates how this path has been modified since the previous successful call to SetTimingsFromVidPn. |
| [DXGK_CRTC_VSYNC_STATE enumeration](ne-d3dkmddi--dxgk-crtc-vsync-state.md) | Provides additional information for DxgkDdi_ControlInterrupt2 when VSYNC is being utilized. |
| [DXGK_CONNECTION_STATUS enumeration](ne-d3dkmddi--dxgk-connection-status.md) | Enumeration indicating the connection status values which can be reported. |
| [DXGK_PROTECTED_SESSION_STATUS enumeration](ne-d3dkmddi--dxgk-protected-session-status.md) | Used to indicate the status of the current session. |
| [DXGK_RECOMMENDVIDPNTOPOLOGY_REASON enumeration](ne-d3dkmddi--dxgk-recommendvidpntopology-reason.md) | Indicates the reason for calling the display miniport driver's DxgkDdiRecommendVidPnTopology function. |
| [DXGK_HANDLE_TYPE enumeration](ne-d3dkmddi--dxgk-handle-type.md) | TBD |
| [DXGK_MONITOR_INTERFACE_VERSION enumeration](ne-d3dkmddi--dxgk-monitor-interface-version.md) | Indicates a particular version of the Monitor interface. |
| [DXGK_WDDMVERSION enumeration](ne-d3dkmddi--dxgk-wddmversion.md) | The DXGK_WDDMVERSION enumeration is reserved for system use. Except for the case noted below, do not use it in your driver. |
| [DXGK_PAGETABLEUPDATEMODE enumeration](ne-d3dkmddi--dxgk-pagetableupdatemode.md) | DXGK_PAGETABLEUPDATEMODE is used as part of a DxgkDdiBuildPagingBuffer operation to indicate which member of the related DXGK_PAGETABLEUPDATEADDRESS structure contains the address of the page table to update. |
| [DXGK_INTERRUPT_STATE enumeration](ne-d3dkmddi--dxgk-interrupt-state.md) | . |
| [DXGK_MEMORY_TRANSFER_DIRECTION enumeration](ne-d3dkmddi--dxgk-memory-transfer-direction.md) | DXGK_MEMORY_TRANSFER_DIRECTION is used as part of an allocation transfer operation to specify the direction of the transfer. |
| [DXGK_GLITCH_CAUSE enumeration](ne-d3dkmddi--dxgk-glitch-cause.md) | Enumeration that describes what caused a glitch during a SetTimingsFromVidPn call. |
| [DXGK_QUERYADAPTERINFOTYPE enumeration](ne-d3dkmddi--dxgk-queryadapterinfotype.md) | The DXGK_QUERYADAPTERINFOTYPE enumeration indicates the type of information to retrieve. |
| [DXGK_GLITCH_DURATION enumeration](ne-d3dkmddi--dxgk-glitch-duration.md) | Enumeration that describes the duration of a user visible effect of a glitch during a SetTimingsFromVidPn call. |
| [DXGK_GDIROP_BITBLT enumeration](ne-d3dkmddi--dxgk-gdirop-bitblt.md) | The DXGK_GDIROP_COLORFILL enumeration indicates the type of GDI raster operation (ROP) to implement in a GDI hardware-accelerated bit-block transfer (bitblt) operation. |
| [DXGK_HARDWARE_CONTENT_PROTECTION_TEARDOWN_FLAGS enumeration](ne-d3dkmddi--dxgk-hardware-content-protection-teardown-flags.md) | DXGK_HARDWARE_CONTENT_PROTECTION_TEARDOWN_FLAGS provides additional information to the driver in a DxgkCbHardwareContentProtectionTeardown call. |
| [DXGK_VIDPN_INTERFACE_VERSION enumeration](ne-d3dkmddi--dxgk-vidpn-interface-version.md) | The DXGK_VIDPN_INTERFACE_VERSION enumeration indicates the version of a video present network (VidPN) interface. |
| [DXGK_RECOMMENDFUNCTIONALVIDPN_REASON enumeration](ne-d3dkmddi--dxgk-recommendfunctionalvidpn-reason.md) | The DXGK_RECOMMENDFUNCTIONALVIDPN_REASON enumeration indicates the reason for calling the display miniport driver's DxgkDdiRecommendFunctionalVidPn function. |
| [DXGK_DISPLAYPANELORIENTATION enumeration](ne-d3dkmddi--dxgk-displaypanelorientation.md) | Enum used to express the orientation of an integrated panel. |
| [DXGK_RENDERKM_OPERATION enumeration](ne-d3dkmddi--dxgk-renderkm-operation.md) | The DXGK_RENDERKM_OPERATION enumeration indicates the type of GDI hardware-accelerated rendering operation to perform when the DxgkDdiRenderKm function is called. |
| [DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration](ne-d3dkmddi--dxgk-multiplane-overlay-stretch-quality.md) | Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data. |
| [DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID enumeration](ne-d3dkmddi--dxgk-present-display-only-progress-id.md) | Indicates the status of the current present operation. |
| [DXGK_BUILDPAGINGBUFFER_OPERATION enumeration](ne-d3dkmddi--dxgk-buildpagingbuffer-operation.md) | Indicates the type of memory operation to perform. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [_Function_class_DXGK_ function](nf-d3dkmddi--function-class-dxgk-.md) | TBD |
| [DXGKNODEMETADATA_GETNODEORDINAL function](nf-d3dkmddi-dxgknodemetadata-getnodeordinal.md) | TBD |
| [DXGKNODEMETADATA_GETPHYSICALADAPTERINDEX function](nf-d3dkmddi-dxgknodemetadata-getphysicaladapterindex.md) | TBD |

This header is used in these topics:

- [display](..content/_display)
